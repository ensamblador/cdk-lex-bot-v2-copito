import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_lex_bot_v2.cdk_lex_bot_v2_stack import CdkLexBotV2Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_lex_bot_v2/cdk_lex_bot_v2_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkLexBotV2Stack(app, "cdk-lex-bot-v2")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
