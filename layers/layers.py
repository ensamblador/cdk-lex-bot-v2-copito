import json
from constructs import Construct

from aws_cdk import (
    aws_lambda

)


class Bs4Requests(Construct):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        #layer con beautiful soup y requests
        bs4_requests = aws_lambda.LayerVersion(
            self, "bs4_requests", code=aws_lambda.Code.from_asset("./layers/bs4_requests.zip"),
            compatible_runtimes = [aws_lambda.Runtime.PYTHON_3_8,aws_lambda.Runtime.PYTHON_3_7], 
            description = 'BeautifulSoup y Requests')

        
        self.layer = bs4_requests


class Pytz(Construct):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        #layer con beautiful soup y requests
        layer = aws_lambda.LayerVersion(
            self, "pytz", code=aws_lambda.Code.from_asset("./layers/pytz-38.zip"),
            compatible_runtimes = [aws_lambda.Runtime.PYTHON_3_8,aws_lambda.Runtime.PYTHON_3_7], 
            description = 'Pytz Python 3.8')

        
        self.layer = layer
