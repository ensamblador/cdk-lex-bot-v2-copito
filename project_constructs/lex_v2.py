import aws_cdk.aws_lex as lex
from constructs import Construct
from aws_cdk import ( 
    CfnTag,  
    Stack,
    aws_iam as iam,
)

from config import (BOT_NAME, DATA_PRIVACY, SENTIMENT_ANALYSYS_SETTINGS, IDLE_SESION_TIMEOUT_IN_SECONDS)
from project_constructs.lex_v2_cloudwatch_logs import CWLogGroup
from project_constructs.lex_v2_lambda_code_hook import LambdaCodeHook
from project_constructs.lex_v2_role import LexV2Role
from project_constructs.lex_v2_s3_deploy import S3BotFiles

print("Bot Name:", BOT_NAME)

data_privacy = DATA_PRIVACY
sentiment_analysis_settings = SENTIMENT_ANALYSYS_SETTINGS
idle_session_ttl_in_seconds = IDLE_SESION_TIMEOUT_IN_SECONDS



class LexBotV2(Construct):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)


        bot_role = LexV2Role(self, 'SLRLexV2')
        s3_bots  = S3BotFiles(self, 's3bots')
        code_hook = LambdaCodeHook(self, 'codeHook')
        log_group = CWLogGroup(self, "logGroup")



        code_hook_specification=lex.CfnBot.CodeHookSpecificationProperty(
            lambda_code_hook=lex.CfnBot.LambdaCodeHookProperty(
                code_hook_interface_version="1.0",
                lambda_arn=code_hook.lambda_function.function_arn
            )
        )
        bot_alias_locale_setting=lex.CfnBot.BotAliasLocaleSettingsProperty(
            enabled=True, code_hook_specification=code_hook_specification
        )

        conversation_log_settings=lex.CfnBot.ConversationLogSettingsProperty(
            audio_log_settings=[lex.CfnBot.AudioLogSettingProperty(
                destination=lex.CfnBot.AudioLogDestinationProperty(
                    s3_bucket=lex.CfnBot.S3BucketLogDestinationProperty(
                        log_prefix=f"{BOT_NAME}/audios",
                        s3_bucket_arn=s3_bots.bucket.bucket_arn,
                    )
                ),
                enabled=True
            )],
            text_log_settings=[lex.CfnBot.TextLogSettingProperty(
                destination=lex.CfnBot.TextLogDestinationProperty(
                    cloud_watch=lex.CfnBot.CloudWatchLogGroupLogDestinationProperty(
                        cloud_watch_log_group_arn=log_group.log_grop.log_group_arn,
                        log_prefix=f"{BOT_NAME}/text"
                    )
                ),
                enabled=True
            )]
        )

        cfn_bot = lex.CfnBot(self, "CfnBot",
            data_privacy = data_privacy,
            idle_session_ttl_in_seconds = idle_session_ttl_in_seconds,
            name=BOT_NAME,
            role_arn=bot_role.arn,
            bot_file_s3_location=lex.CfnBot.S3LocationProperty(
                s3_bucket=s3_bots.s3deploy.deployed_bucket.bucket_name,
                s3_object_key=s3_bots.key['copito']),
            auto_build_bot_locales=True,
            description=f"{BOT_NAME}-CDK Generado",
            test_bot_alias_settings=lex.CfnBot.TestBotAliasSettingsProperty(
                bot_alias_locale_settings=[lex.CfnBot.BotAliasLocaleSettingsItemProperty(
                    bot_alias_locale_setting= bot_alias_locale_setting, 
                    locale_id="es_US"
                )],
                conversation_log_settings = conversation_log_settings,
                sentiment_analysis_settings=SENTIMENT_ANALYSYS_SETTINGS
            )
        )

        code_hook.lambda_function.add_permission(
            principal=iam.ServicePrincipal("lexv2.amazonaws.com"),id='bot-invoke',
            action='lambda:InvokeFunction', source_arn = f"arn:aws:lex:{Stack.of(self).region}:{Stack.of(self).account}:bot-alias/*"
            )

        
        cfn_bot.node.add_dependency(bot_role.role)
        cfn_bot.node.add_dependency(s3_bots.s3deploy.deployed_bucket)
        
