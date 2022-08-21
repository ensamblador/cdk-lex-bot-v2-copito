import boto3

import aws_cdk.aws_lex as lex

from constructs import Construct
from aws_cdk import ( aws_iam as iam, Stack)


class LexV2Role(Construct):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        
        crea_rol = True
        account_id = Stack.of(self).account
        
        role_name = "AWSServiceRoleForLexV2Bots"
        """
        try:
            existing_role = boto3.client('iam').get_role(RoleName = role_name)
            print ('role encontrado',existing_role['Role']['Arn'])
            self.arn = existing_role['Role']['Arn']
        except:
            print('No Existe')
            crea_rol = True
        """
        if crea_rol:
            self.arn = f'arn:aws:iam::{account_id}:role/aws-service-role/lexv2.amazonaws.com/AWSServiceRoleForLexV2Bots'
            bot_role = iam.CfnServiceLinkedRole( self, 'BotRole',
                aws_service_name='lexv2.amazonaws.com',
                #custom_suffix="_new"
            )
            self.role = bot_role
        
        else:
            bot_role = iam.Role.from_role_name(self, 'SLRExistente', role_name=role_name)
            self.role = bot_role
        