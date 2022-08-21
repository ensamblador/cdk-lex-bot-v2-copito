from aws_cdk import (Duration,aws_lambda)

BOT_NAME = 'Agendar'

DATA_PRIVACY = {'ChildDirected': False}
SENTIMENT_ANALYSYS_SETTINGS = {}
IDLE_SESION_TIMEOUT_IN_SECONDS = 120

STACK_NAME = f'LEX-V2-{BOT_NAME.upper()}'

TAGS =  {
    "APPLICATION": "CER",
    "ENVIRONMENT": "DEV",
    "GROUP": "BOTS"
}


BASE_LAMBDA_CONFIG = dict (
    timeout=Duration.seconds(8),       
    memory_size=256,
    tracing= aws_lambda.Tracing.ACTIVE)

PYTHON_LAMBDA_CONFIG = dict(
    runtime=aws_lambda.Runtime.PYTHON_3_8, 
    **BASE_LAMBDA_CONFIG)
