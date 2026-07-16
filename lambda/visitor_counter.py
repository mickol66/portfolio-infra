import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('SiteVisitors')

def lambda_handler(event, context):
    try:
        # Öka räknaren för raden med Id "total_visits" med +1.
        response = table.update_item(
            Key={'Id': 'total_visits'},
            UpdateExpression="SET views = if_not_exists(views, :start) + :inc",
            ExpressionAttributeValues={
                ':inc': 1,
                ':start': 0
            },
            ReturnValues="UPDATED_NEW"
        )
        
        current_views = int(response['Attributes']['views'])
        
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'OPTIONS,POST'
            },
            'body': json.dumps({'views': current_views})
        }
        
    except Exception as e:
        print(f"Fel i besöksräknaren: {str(e)}")
        return {
            'statusCode': 500,
            'headers': { 'Access-Control-Allow-Origin': '*' },
            'body': json.dumps({'error': 'Kunde inte uppdatera besöksräknaren'})
        }

