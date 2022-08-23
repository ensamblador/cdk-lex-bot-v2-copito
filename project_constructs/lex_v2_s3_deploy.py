from constructs import Construct
from aws_cdk import ( aws_iam as iam,aws_s3_deployment as s3deploy, aws_s3 as s3, RemovalPolicy)


class S3BotFiles(Construct):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self.bucket = s3.Bucket(self, "b", removal_policy=RemovalPolicy.DESTROY)

        self.s3deploy = s3deploy.BucketDeployment(self, "DeployWebsite",
            sources=[s3deploy.Source.asset("./bot_files")],
            destination_bucket=self.bucket,
            destination_key_prefix="bot_files"
        )
        self.key = {
            "agenda": "bot_files/agendar-cita-es.zip",
            "copito": "bot_files/copito-indicadores.zip",
            }


