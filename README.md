# Serverless Portfolio Infrastructure (AWS CDK & Python)

This repository contains the complete **Infrastructure as Code (IaC)** for my cloud portfolio project. Using the **AWS Cloud Development Kit (CDK) with Python**, I have fully automated the provisioning of a secure, scalable, and highly available serverless backend.

## 📐 Architecture & Services
The backend is designed around the AWS Well-Architected Framework, prioritizing cost-efficiency (100% Free-Tier eligible under normal traffic) and zero server management.

![AWS Architecture Diagram](architectural-diagram.png)
_Architecture diagram automated and generated using **AWS Kiro CLI** and **Model Context Protocol (MCP)**._

### Infrastructure Components:
* **Amazon Route 53 & ACM:** Manages DNS routing and provisions free SSL/TLS certificates for end-to-end encryption.
* **Amazon CloudFront & S3:** Serves the static website globally with low latency. CloudFront Functions are attached to handle clean URL rewrites and strict Security Headers (achieving an **A-Rating**).
* **Amazon API Gateway:** Exposes secure REST endpoints (`/contact` and `/visit`) protected with proper CORS configurations.
* **AWS Lambda (Python):** Handles backend execution on-demand. Written using `boto3`, featuring safe asynchronous database updates.
* **Amazon DynamoDB:** A highly scalable NoSQL database. Leverages advanced expressions (like `update_item` with expression attributes) to atomicly increment counts and handle reserved database keywords safely.
* **Amazon SES (Simple Email Service):** Forwards user contact form inputs directly to my personal inbox.

## 🚀 How to Deploy (IaC)
Because this project utilizes AWS CDK, the entire environment can be bootstrapped and deployed to any AWS region with a single command from the terminal.

```bash
# Install dependencies
pip install -r requirements.txt

# Bootstrap the region (first time only)
npx cdk bootstrap

# Deploy the complete architecture to AWS
npx cdk deploy
```

---

## 🖥️ Looking for the Website Code?
The user interface and CI/CD deployment pipeline for the frontend are hosted in a separate repository.
👉 Check out the web code here: [mickol66/aws_github](https://github.com/mickol66/aws_github.readme.md)
