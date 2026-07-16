from aws_cdk import (
    Stack,
    aws_dynamodb as dynamodb,
    aws_lambda as _lambda,
    aws_apigateway as apigateway,
    RemovalPolicy
)
from constructs import Construct

class PortfolioInfraStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # 1. Skapa DynamoDB-tabell för besökare via IaC
        visitors_table = dynamodb.Table(
            self, "VisitorsTable",
            table_name="SiteVisitors",
            partition_key=dynamodb.Attribute(name="Id", type=dynamodb.AttributeType.STRING),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
            removal_policy=RemovalPolicy.DESTROY
        )

        # 2. Skapa Lambda-funktionen via IaC
        visitor_lambda = _lambda.Function(
            self, "VisitorCounterFunction",
            runtime=_lambda.Runtime.PYTHON_3_11,
            handler="visitor_counter.lambda_handler",
            code=_lambda.Code.from_asset("lambda")
        )

        # Ge Lambda-funktionen rättighet att läsa/skriva i tabellen
        visitors_table.grant_read_write_data(visitor_lambda)

        # 3. Skapa API Gateway (REST API) via IaC
        api = apigateway.RestApi(
            self, "VisitorApi",
            default_cors_preflight_options=apigateway.CorsOptions(
                allow_origins=apigateway.Cors.ALL_ORIGINS,
                allow_methods=["GET", "POST", "OPTIONS"]
            )
        )

        # Skapa en /visit slutpunkt och koppla till Lambda
        visit_resource = api.root.add_resource("visit")
        visit_resource.add_method("POST", apigateway.LambdaIntegration(visitor_lambda))

