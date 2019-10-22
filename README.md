# Lambda Edge Function for CloudFront origin-request

- Implements blue/green with single CloudFront distribution with multiple S3 origins
- Set default index.html object for not only root directory but also sub-directories

Assumption:
- domain: yourdomain.com
- blue domain: blue.yourdomain.com
- green domain: green.yourdomain.com
- S3 bucket for blue origin: your-blue-bucket
- S3 bucket for green origin: your-green-bucket

## Dependency

- python3

## Create Deploy Package

```
rm origin_request.zip
zip origin_request.zip main.py
``

## Deploy

```
# lambda edge only in region us-east-1
aws --region us-east-1 s3 cp origin_request.zip s3://your-s3-bucket-for-lambda-edge-package/
aws --region us-east-1 lambda update-function-code --s3-bucket your-s3-bucket-for-lambda-edge-package --s3-key origin_request.zip --function-name your_lambda_edge_function_name
aws --region us-east-1 lambda publish-version --function-name your_lambda_edge_function_name
```

## Test
```
python3 -m unittest discover test
```
