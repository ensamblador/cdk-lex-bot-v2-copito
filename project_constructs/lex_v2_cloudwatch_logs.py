from constructs import Construct
from aws_cdk import ( aws_iam as iam, aws_logs as logs, RemovalPolicy)

from config import (PYTHON_LAMBDA_CONFIG)

class CWLogGroup(Construct):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self.log_grop  = logs.LogGroup(self, "Log Group", removal_policy=RemovalPolicy.DESTROY)

