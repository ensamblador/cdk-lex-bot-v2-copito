from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
)
from constructs import Construct
from project_constructs.lex_v2 import LexBotV2


class CdkLexBotV2Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        lexBoxCopito = LexBotV2(self, 'bot_copito', 'copito')


