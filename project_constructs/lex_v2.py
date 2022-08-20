from typing import Any
import aws_cdk.aws_lex as lex
from constructs import Construct
from aws_cdk import ( 
    CfnTag,  
    aws_iam as iam,
)


from config import BOT_NAME

print("Bot Name:", BOT_NAME)

data_privacy = {}
sentiment_analysis_settings = Any
idle_session_ttl_in_seconds=120



class LexBotV2(Construct):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)



        bot_role = iam.CfnServiceLinkedRole( self, 'BotRole',
            aws_service_name='lexv2.amazonaws.com',
            #custom_suffix="_new"
        )
        #arn = 'arn:aws:iam::448716646650:role/aws-service-role/lexv2.amazonaws.com/AWSServiceRoleForLexV2Bots'
        print(bot_role.logical_id, bot_role.get_att('resource.arn'))
        
        cfn_bot = lex.CfnBot(self, "CfnBot",
            data_privacy = data_privacy,
            idle_session_ttl_in_seconds = idle_session_ttl_in_seconds,
            name=BOT_NAME,
            role_arn=bot_role.get_att('arn').to_string()
        )
        """ 
                # the properties below are optional
                auto_build_bot_locales=False,
                bot_file_s3_location=lex.CfnBot.S3LocationProperty(
                    s3_bucket="s3Bucket",
                    s3_object_key="s3ObjectKey",

                    # the properties below are optional
                    s3_object_version="s3ObjectVersion"
                ),
                bot_locales=[lex.CfnBot.BotLocaleProperty(
                    locale_id="localeId",
                    nlu_confidence_threshold=123,

                    # the properties below are optional
                    custom_vocabulary=lex.CfnBot.CustomVocabularyProperty(
                        custom_vocabulary_items=[lex.CfnBot.CustomVocabularyItemProperty(
                            phrase="phrase",

                            # the properties below are optional
                            weight=123
                        )]
                    ),
                    description="description",
                    intents=[lex.CfnBot.IntentProperty(
                        name="name",

                        # the properties below are optional
                        description="description",
                        dialog_code_hook=lex.CfnBot.DialogCodeHookSettingProperty(
                            enabled=False
                        ),
                        fulfillment_code_hook=lex.CfnBot.FulfillmentCodeHookSettingProperty(
                            enabled=False,

                            # the properties below are optional
                            fulfillment_updates_specification=lex.CfnBot.FulfillmentUpdatesSpecificationProperty(
                                active=False,

                                # the properties below are optional
                                start_response=lex.CfnBot.FulfillmentStartResponseSpecificationProperty(
                                    delay_in_seconds=123,
                                    message_groups=[lex.CfnBot.MessageGroupProperty(
                                        message=lex.CfnBot.MessageProperty(
                                            custom_payload=lex.CfnBot.CustomPayloadProperty(
                                                value="value"
                                            ),
                                            image_response_card=lex.CfnBot.ImageResponseCardProperty(
                                                title="title",

                                                # the properties below are optional
                                                buttons=[lex.CfnBot.ButtonProperty(
                                                    text="text",
                                                    value="value"
                                                )],
                                                image_url="imageUrl",
                                                subtitle="subtitle"
                                            ),
                                            plain_text_message=lex.CfnBot.PlainTextMessageProperty(
                                                value="value"
                                            ),
                                            ssml_message=lex.CfnBot.SSMLMessageProperty(
                                                value="value"
                                            )
                                        ),

                                        # the properties below are optional
                                        variations=[lex.CfnBot.MessageProperty(
                                            custom_payload=lex.CfnBot.CustomPayloadProperty(
                                                value="value"
                                            ),
                                            image_response_card=lex.CfnBot.ImageResponseCardProperty(
                                                title="title",

                                                # the properties below are optional
                                                buttons=[lex.CfnBot.ButtonProperty(
                                                    text="text",
                                                    value="value"
                                                )],
                                                image_url="imageUrl",
                                                subtitle="subtitle"
                                            ),
                                            plain_text_message=lex.CfnBot.PlainTextMessageProperty(
                                                value="value"
                                            ),
                                            ssml_message=lex.CfnBot.SSMLMessageProperty(
                                                value="value"
                                            )
                                        )]
                                    )],

                                    # the properties below are optional
                                    allow_interrupt=False
                                ),
                                timeout_in_seconds=123,
                                update_response=lex.CfnBot.FulfillmentUpdateResponseSpecificationProperty(
                                    frequency_in_seconds=123,
                                    message_groups=[lex.CfnBot.MessageGroupProperty(
                                        message=lex.CfnBot.MessageProperty(
                                            custom_payload=lex.CfnBot.CustomPayloadProperty(
                                                value="value"
                                            ),
                                            image_response_card=lex.CfnBot.ImageResponseCardProperty(
                                                title="title",

                                                # the properties below are optional
                                                buttons=[lex.CfnBot.ButtonProperty(
                                                    text="text",
                                                    value="value"
                                                )],
                                                image_url="imageUrl",
                                                subtitle="subtitle"
                                            ),
                                            plain_text_message=lex.CfnBot.PlainTextMessageProperty(
                                                value="value"
                                            ),
                                            ssml_message=lex.CfnBot.SSMLMessageProperty(
                                                value="value"
                                            )
                                        ),

                                        # the properties below are optional
                                        variations=[lex.CfnBot.MessageProperty(
                                            custom_payload=lex.CfnBot.CustomPayloadProperty(
                                                value="value"
                                            ),
                                            image_response_card=lex.CfnBot.ImageResponseCardProperty(
                                                title="title",

                                                # the properties below are optional
                                                buttons=[lex.CfnBot.ButtonProperty(
                                                    text="text",
                                                    value="value"
                                                )],
                                                image_url="imageUrl",
                                                subtitle="subtitle"
                                            ),
                                            plain_text_message=lex.CfnBot.PlainTextMessageProperty(
                                                value="value"
                                            ),
                                            ssml_message=lex.CfnBot.SSMLMessageProperty(
                                                value="value"
                                            )
                                        )]
                                    )],

                                    # the properties below are optional
                                    allow_interrupt=False
                                )
                            ),
                            post_fulfillment_status_specification=lex.CfnBot.PostFulfillmentStatusSpecificationProperty(
                                failure_response=lex.CfnBot.ResponseSpecificationProperty(
                                    message_groups_list=[lex.CfnBot.MessageGroupProperty(
                                        message=lex.CfnBot.MessageProperty(
                                            custom_payload=lex.CfnBot.CustomPayloadProperty(
                                                value="value"
                                            ),
                                            image_response_card=lex.CfnBot.ImageResponseCardProperty(
                                                title="title",

                                                # the properties below are optional
                                                buttons=[lex.CfnBot.ButtonProperty(
                                                    text="text",
                                                    value="value"
                                                )],
                                                image_url="imageUrl",
                                                subtitle="subtitle"
                                            ),
                                            plain_text_message=lex.CfnBot.PlainTextMessageProperty(
                                                value="value"
                                            ),
                                            ssml_message=lex.CfnBot.SSMLMessageProperty(
                                                value="value"
                                            )
                                        ),

                                        # the properties below are optional
                                        variations=[lex.CfnBot.MessageProperty(
                                            custom_payload=lex.CfnBot.CustomPayloadProperty(
                                                value="value"
                                            ),
                                            image_response_card=lex.CfnBot.ImageResponseCardProperty(
                                                title="title",

                                                # the properties below are optional
                                                buttons=[lex.CfnBot.ButtonProperty(
                                                    text="text",
                                                    value="value"
                                                )],
                                                image_url="imageUrl",
                                                subtitle="subtitle"
                                            ),
                                            plain_text_message=lex.CfnBot.PlainTextMessageProperty(
                                                value="value"
                                            ),
                                            ssml_message=lex.CfnBot.SSMLMessageProperty(
                                                value="value"
                                            )
                                        )]
                                    )],

                                    # the properties below are optional
                                    allow_interrupt=False
                                ),
                                success_response=lex.CfnBot.ResponseSpecificationProperty(
                                    message_groups_list=[lex.CfnBot.MessageGroupProperty(
                                        message=lex.CfnBot.MessageProperty(
                                            custom_payload=lex.CfnBot.CustomPayloadProperty(
                                                value="value"
                                            ),
                                            image_response_card=lex.CfnBot.ImageResponseCardProperty(
                                                title="title",

                                                # the properties below are optional
                                                buttons=[lex.CfnBot.ButtonProperty(
                                                    text="text",
                                                    value="value"
                                                )],
                                                image_url="imageUrl",
                                                subtitle="subtitle"
                                            ),
                                            plain_text_message=lex.CfnBot.PlainTextMessageProperty(
                                                value="value"
                                            ),
                                            ssml_message=lex.CfnBot.SSMLMessageProperty(
                                                value="value"
                                            )
                                        ),

                                        # the properties below are optional
                                        variations=[lex.CfnBot.MessageProperty(
                                            custom_payload=lex.CfnBot.CustomPayloadProperty(
                                                value="value"
                                            ),
                                            image_response_card=lex.CfnBot.ImageResponseCardProperty(
                                                title="title",

                                                # the properties below are optional
                                                buttons=[lex.CfnBot.ButtonProperty(
                                                    text="text",
                                                    value="value"
                                                )],
                                                image_url="imageUrl",
                                                subtitle="subtitle"
                                            ),
                                            plain_text_message=lex.CfnBot.PlainTextMessageProperty(
                                                value="value"
                                            ),
                                            ssml_message=lex.CfnBot.SSMLMessageProperty(
                                                value="value"
                                            )
                                        )]
                                    )],

                                    # the properties below are optional
                                    allow_interrupt=False
                                ),
                                timeout_response=lex.CfnBot.ResponseSpecificationProperty(
                                    message_groups_list=[lex.CfnBot.MessageGroupProperty(
                                        message=lex.CfnBot.MessageProperty(
                                            custom_payload=lex.CfnBot.CustomPayloadProperty(
                                                value="value"
                                            ),
                                            image_response_card=lex.CfnBot.ImageResponseCardProperty(
                                                title="title",

                                                # the properties below are optional
                                                buttons=[lex.CfnBot.ButtonProperty(
                                                    text="text",
                                                    value="value"
                                                )],
                                                image_url="imageUrl",
                                                subtitle="subtitle"
                                            ),
                                            plain_text_message=lex.CfnBot.PlainTextMessageProperty(
                                                value="value"
                                            ),
                                            ssml_message=lex.CfnBot.SSMLMessageProperty(
                                                value="value"
                                            )
                                        ),

                                        # the properties below are optional
                                        variations=[lex.CfnBot.MessageProperty(
                                            custom_payload=lex.CfnBot.CustomPayloadProperty(
                                                value="value"
                                            ),
                                            image_response_card=lex.CfnBot.ImageResponseCardProperty(
                                                title="title",

                                                # the properties below are optional
                                                buttons=[lex.CfnBot.ButtonProperty(
                                                    text="text",
                                                    value="value"
                                                )],
                                                image_url="imageUrl",
                                                subtitle="subtitle"
                                            ),
                                            plain_text_message=lex.CfnBot.PlainTextMessageProperty(
                                                value="value"
                                            ),
                                            ssml_message=lex.CfnBot.SSMLMessageProperty(
                                                value="value"
                                            )
                                        )]
                                    )],

                                    # the properties below are optional
                                    allow_interrupt=False
                                )
                            )
                        ),
                        input_contexts=[lex.CfnBot.InputContextProperty(
                            name="name"
                        )],
                        intent_closing_setting=lex.CfnBot.IntentClosingSettingProperty(
                            closing_response=lex.CfnBot.ResponseSpecificationProperty(
                                message_groups_list=[lex.CfnBot.MessageGroupProperty(
                                    message=lex.CfnBot.MessageProperty(
                                        custom_payload=lex.CfnBot.CustomPayloadProperty(
                                            value="value"
                                        ),
                                        image_response_card=lex.CfnBot.ImageResponseCardProperty(
                                            title="title",

                                            # the properties below are optional
                                            buttons=[lex.CfnBot.ButtonProperty(
                                                text="text",
                                                value="value"
                                            )],
                                            image_url="imageUrl",
                                            subtitle="subtitle"
                                        ),
                                        plain_text_message=lex.CfnBot.PlainTextMessageProperty(
                                            value="value"
                                        ),
                                        ssml_message=lex.CfnBot.SSMLMessageProperty(
                                            value="value"
                                        )
                                    ),

                                    # the properties below are optional
                                    variations=[lex.CfnBot.MessageProperty(
                                        custom_payload=lex.CfnBot.CustomPayloadProperty(
                                            value="value"
                                        ),
                                        image_response_card=lex.CfnBot.ImageResponseCardProperty(
                                            title="title",

                                            # the properties below are optional
                                            buttons=[lex.CfnBot.ButtonProperty(
                                                text="text",
                                                value="value"
                                            )],
                                            image_url="imageUrl",
                                            subtitle="subtitle"
                                        ),
                                        plain_text_message=lex.CfnBot.PlainTextMessageProperty(
                                            value="value"
                                        ),
                                        ssml_message=lex.CfnBot.SSMLMessageProperty(
                                            value="value"
                                        )
                                    )]
                                )],

                                # the properties below are optional
                                allow_interrupt=False
                            ),

                            # the properties below are optional
                            is_active=False
                        ),
                        intent_confirmation_setting=lex.CfnBot.IntentConfirmationSettingProperty(
                            declination_response=lex.CfnBot.ResponseSpecificationProperty(
                                message_groups_list=[lex.CfnBot.MessageGroupProperty(
                                    message=lex.CfnBot.MessageProperty(
                                        custom_payload=lex.CfnBot.CustomPayloadProperty(
                                            value="value"
                                        ),
                                        image_response_card=lex.CfnBot.ImageResponseCardProperty(
                                            title="title",

                                            # the properties below are optional
                                            buttons=[lex.CfnBot.ButtonProperty(
                                                text="text",
                                                value="value"
                                            )],
                                            image_url="imageUrl",
                                            subtitle="subtitle"
                                        ),
                                        plain_text_message=lex.CfnBot.PlainTextMessageProperty(
                                            value="value"
                                        ),
                                        ssml_message=lex.CfnBot.SSMLMessageProperty(
                                            value="value"
                                        )
                                    ),

                                    # the properties below are optional
                                    variations=[lex.CfnBot.MessageProperty(
                                        custom_payload=lex.CfnBot.CustomPayloadProperty(
                                            value="value"
                                        ),
                                        image_response_card=lex.CfnBot.ImageResponseCardProperty(
                                            title="title",

                                            # the properties below are optional
                                            buttons=[lex.CfnBot.ButtonProperty(
                                                text="text",
                                                value="value"
                                            )],
                                            image_url="imageUrl",
                                            subtitle="subtitle"
                                        ),
                                        plain_text_message=lex.CfnBot.PlainTextMessageProperty(
                                            value="value"
                                        ),
                                        ssml_message=lex.CfnBot.SSMLMessageProperty(
                                            value="value"
                                        )
                                    )]
                                )],

                                # the properties below are optional
                                allow_interrupt=False
                            ),
                            prompt_specification=lex.CfnBot.PromptSpecificationProperty(
                                max_retries=123,
                                message_groups_list=[lex.CfnBot.MessageGroupProperty(
                                    message=lex.CfnBot.MessageProperty(
                                        custom_payload=lex.CfnBot.CustomPayloadProperty(
                                            value="value"
                                        ),
                                        image_response_card=lex.CfnBot.ImageResponseCardProperty(
                                            title="title",

                                            # the properties below are optional
                                            buttons=[lex.CfnBot.ButtonProperty(
                                                text="text",
                                                value="value"
                                            )],
                                            image_url="imageUrl",
                                            subtitle="subtitle"
                                        ),
                                        plain_text_message=lex.CfnBot.PlainTextMessageProperty(
                                            value="value"
                                        ),
                                        ssml_message=lex.CfnBot.SSMLMessageProperty(
                                            value="value"
                                        )
                                    ),

                                    # the properties below are optional
                                    variations=[lex.CfnBot.MessageProperty(
                                        custom_payload=lex.CfnBot.CustomPayloadProperty(
                                            value="value"
                                        ),
                                        image_response_card=lex.CfnBot.ImageResponseCardProperty(
                                            title="title",

                                            # the properties below are optional
                                            buttons=[lex.CfnBot.ButtonProperty(
                                                text="text",
                                                value="value"
                                            )],
                                            image_url="imageUrl",
                                            subtitle="subtitle"
                                        ),
                                        plain_text_message=lex.CfnBot.PlainTextMessageProperty(
                                            value="value"
                                        ),
                                        ssml_message=lex.CfnBot.SSMLMessageProperty(
                                            value="value"
                                        )
                                    )]
                                )],

                                # the properties below are optional
                                allow_interrupt=False,
                                message_selection_strategy="messageSelectionStrategy"
                            ),

                            # the properties below are optional
                            is_active=False
                        ),
                        kendra_configuration=lex.CfnBot.KendraConfigurationProperty(
                            kendra_index="kendraIndex",

                            # the properties below are optional
                            query_filter_string="queryFilterString",
                            query_filter_string_enabled=False
                        ),
                        output_contexts=[lex.CfnBot.OutputContextProperty(
                            name="name",
                            time_to_live_in_seconds=123,
                            turns_to_live=123
                        )],
                        parent_intent_signature="parentIntentSignature",
                        sample_utterances=[lex.CfnBot.SampleUtteranceProperty(
                            utterance="utterance"
                        )],
                        slot_priorities=[lex.CfnBot.SlotPriorityProperty(
                            priority=123,
                            slot_name="slotName"
                        )],
                        slots=[lex.CfnBot.SlotProperty(
                            name="name",
                            slot_type_name="slotTypeName",
                            value_elicitation_setting=lex.CfnBot.SlotValueElicitationSettingProperty(
                                slot_constraint="slotConstraint",

                                # the properties below are optional
                                default_value_specification=lex.CfnBot.SlotDefaultValueSpecificationProperty(
                                    default_value_list=[lex.CfnBot.SlotDefaultValueProperty(
                                        default_value="defaultValue"
                                    )]
                                ),
                                prompt_specification=lex.CfnBot.PromptSpecificationProperty(
                                    max_retries=123,
                                    message_groups_list=[lex.CfnBot.MessageGroupProperty(
                                        message=lex.CfnBot.MessageProperty(
                                            custom_payload=lex.CfnBot.CustomPayloadProperty(
                                                value="value"
                                            ),
                                            image_response_card=lex.CfnBot.ImageResponseCardProperty(
                                                title="title",

                                                # the properties below are optional
                                                buttons=[lex.CfnBot.ButtonProperty(
                                                    text="text",
                                                    value="value"
                                                )],
                                                image_url="imageUrl",
                                                subtitle="subtitle"
                                            ),
                                            plain_text_message=lex.CfnBot.PlainTextMessageProperty(
                                                value="value"
                                            ),
                                            ssml_message=lex.CfnBot.SSMLMessageProperty(
                                                value="value"
                                            )
                                        ),

                                        # the properties below are optional
                                        variations=[lex.CfnBot.MessageProperty(
                                            custom_payload=lex.CfnBot.CustomPayloadProperty(
                                                value="value"
                                            ),
                                            image_response_card=lex.CfnBot.ImageResponseCardProperty(
                                                title="title",

                                                # the properties below are optional
                                                buttons=[lex.CfnBot.ButtonProperty(
                                                    text="text",
                                                    value="value"
                                                )],
                                                image_url="imageUrl",
                                                subtitle="subtitle"
                                            ),
                                            plain_text_message=lex.CfnBot.PlainTextMessageProperty(
                                                value="value"
                                            ),
                                            ssml_message=lex.CfnBot.SSMLMessageProperty(
                                                value="value"
                                            )
                                        )]
                                    )],

                                    # the properties below are optional
                                    allow_interrupt=False,
                                    message_selection_strategy="messageSelectionStrategy"
                                ),
                                sample_utterances=[lex.CfnBot.SampleUtteranceProperty(
                                    utterance="utterance"
                                )],
                                wait_and_continue_specification=lex.CfnBot.WaitAndContinueSpecificationProperty(
                                    continue_response=lex.CfnBot.ResponseSpecificationProperty(
                                        message_groups_list=[lex.CfnBot.MessageGroupProperty(
                                            message=lex.CfnBot.MessageProperty(
                                                custom_payload=lex.CfnBot.CustomPayloadProperty(
                                                    value="value"
                                                ),
                                                image_response_card=lex.CfnBot.ImageResponseCardProperty(
                                                    title="title",

                                                    # the properties below are optional
                                                    buttons=[lex.CfnBot.ButtonProperty(
                                                        text="text",
                                                        value="value"
                                                    )],
                                                    image_url="imageUrl",
                                                    subtitle="subtitle"
                                                ),
                                                plain_text_message=lex.CfnBot.PlainTextMessageProperty(
                                                    value="value"
                                                ),
                                                ssml_message=lex.CfnBot.SSMLMessageProperty(
                                                    value="value"
                                                )
                                            ),

                                            # the properties below are optional
                                            variations=[lex.CfnBot.MessageProperty(
                                                custom_payload=lex.CfnBot.CustomPayloadProperty(
                                                    value="value"
                                                ),
                                                image_response_card=lex.CfnBot.ImageResponseCardProperty(
                                                    title="title",

                                                    # the properties below are optional
                                                    buttons=[lex.CfnBot.ButtonProperty(
                                                        text="text",
                                                        value="value"
                                                    )],
                                                    image_url="imageUrl",
                                                    subtitle="subtitle"
                                                ),
                                                plain_text_message=lex.CfnBot.PlainTextMessageProperty(
                                                    value="value"
                                                ),
                                                ssml_message=lex.CfnBot.SSMLMessageProperty(
                                                    value="value"
                                                )
                                            )]
                                        )],

                                        # the properties below are optional
                                        allow_interrupt=False
                                    ),
                                    waiting_response=lex.CfnBot.ResponseSpecificationProperty(
                                        message_groups_list=[lex.CfnBot.MessageGroupProperty(
                                            message=lex.CfnBot.MessageProperty(
                                                custom_payload=lex.CfnBot.CustomPayloadProperty(
                                                    value="value"
                                                ),
                                                image_response_card=lex.CfnBot.ImageResponseCardProperty(
                                                    title="title",

                                                    # the properties below are optional
                                                    buttons=[lex.CfnBot.ButtonProperty(
                                                        text="text",
                                                        value="value"
                                                    )],
                                                    image_url="imageUrl",
                                                    subtitle="subtitle"
                                                ),
                                                plain_text_message=lex.CfnBot.PlainTextMessageProperty(
                                                    value="value"
                                                ),
                                                ssml_message=lex.CfnBot.SSMLMessageProperty(
                                                    value="value"
                                                )
                                            ),

                                            # the properties below are optional
                                            variations=[lex.CfnBot.MessageProperty(
                                                custom_payload=lex.CfnBot.CustomPayloadProperty(
                                                    value="value"
                                                ),
                                                image_response_card=lex.CfnBot.ImageResponseCardProperty(
                                                    title="title",

                                                    # the properties below are optional
                                                    buttons=[lex.CfnBot.ButtonProperty(
                                                        text="text",
                                                        value="value"
                                                    )],
                                                    image_url="imageUrl",
                                                    subtitle="subtitle"
                                                ),
                                                plain_text_message=lex.CfnBot.PlainTextMessageProperty(
                                                    value="value"
                                                ),
                                                ssml_message=lex.CfnBot.SSMLMessageProperty(
                                                    value="value"
                                                )
                                            )]
                                        )],

                                        # the properties below are optional
                                        allow_interrupt=False
                                    ),

                                    # the properties below are optional
                                    is_active=False,
                                    still_waiting_response=lex.CfnBot.StillWaitingResponseSpecificationProperty(
                                        frequency_in_seconds=123,
                                        message_groups_list=[lex.CfnBot.MessageGroupProperty(
                                            message=lex.CfnBot.MessageProperty(
                                                custom_payload=lex.CfnBot.CustomPayloadProperty(
                                                    value="value"
                                                ),
                                                image_response_card=lex.CfnBot.ImageResponseCardProperty(
                                                    title="title",

                                                    # the properties below are optional
                                                    buttons=[lex.CfnBot.ButtonProperty(
                                                        text="text",
                                                        value="value"
                                                    )],
                                                    image_url="imageUrl",
                                                    subtitle="subtitle"
                                                ),
                                                plain_text_message=lex.CfnBot.PlainTextMessageProperty(
                                                    value="value"
                                                ),
                                                ssml_message=lex.CfnBot.SSMLMessageProperty(
                                                    value="value"
                                                )
                                            ),

                                            # the properties below are optional
                                            variations=[lex.CfnBot.MessageProperty(
                                                custom_payload=lex.CfnBot.CustomPayloadProperty(
                                                    value="value"
                                                ),
                                                image_response_card=lex.CfnBot.ImageResponseCardProperty(
                                                    title="title",

                                                    # the properties below are optional
                                                    buttons=[lex.CfnBot.ButtonProperty(
                                                        text="text",
                                                        value="value"
                                                    )],
                                                    image_url="imageUrl",
                                                    subtitle="subtitle"
                                                ),
                                                plain_text_message=lex.CfnBot.PlainTextMessageProperty(
                                                    value="value"
                                                ),
                                                ssml_message=lex.CfnBot.SSMLMessageProperty(
                                                    value="value"
                                                )
                                            )]
                                        )],
                                        timeout_in_seconds=123,

                                        # the properties below are optional
                                        allow_interrupt=False
                                    )
                                )
                            ),

                            # the properties below are optional
                            description="description",
                            multiple_values_setting=lex.CfnBot.MultipleValuesSettingProperty(
                                allow_multiple_values=False
                            ),
                            obfuscation_setting=lex.CfnBot.ObfuscationSettingProperty(
                                obfuscation_setting_type="obfuscationSettingType"
                            )
                        )]
                    )],
                    slot_types=[lex.CfnBot.SlotTypeProperty(
                        name="name",

                        # the properties below are optional
                        description="description",
                        external_source_setting=lex.CfnBot.ExternalSourceSettingProperty(
                            grammar_slot_type_setting=lex.CfnBot.GrammarSlotTypeSettingProperty(
                                source=lex.CfnBot.GrammarSlotTypeSourceProperty(
                                    s3_bucket_name="s3BucketName",
                                    s3_object_key="s3ObjectKey",

                                    # the properties below are optional
                                    kms_key_arn="kmsKeyArn"
                                )
                            )
                        ),
                        parent_slot_type_signature="parentSlotTypeSignature",
                        slot_type_values=[lex.CfnBot.SlotTypeValueProperty(
                            sample_value=lex.CfnBot.SampleValueProperty(
                                value="value"
                            ),

                            # the properties below are optional
                            synonyms=[lex.CfnBot.SampleValueProperty(
                                value="value"
                            )]
                        )],
                        value_selection_setting=lex.CfnBot.SlotValueSelectionSettingProperty(
                            resolution_strategy="resolutionStrategy",

                            # the properties below are optional
                            advanced_recognition_setting=lex.CfnBot.AdvancedRecognitionSettingProperty(
                                audio_recognition_strategy="audioRecognitionStrategy"
                            ),
                            regex_filter=lex.CfnBot.SlotValueRegexFilterProperty(
                                pattern="pattern"
                            )
                        )
                    )],
                    voice_settings=lex.CfnBot.VoiceSettingsProperty(
                        voice_id="voiceId"
                    )
                )],
                bot_tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                description="description",
                test_bot_alias_settings=lex.CfnBot.TestBotAliasSettingsProperty(
                    bot_alias_locale_settings=[lex.CfnBot.BotAliasLocaleSettingsItemProperty(
                        bot_alias_locale_setting=lex.CfnBot.BotAliasLocaleSettingsProperty(
                            enabled=False,

                            # the properties below are optional
                            code_hook_specification=lex.CfnBot.CodeHookSpecificationProperty(
                                lambda_code_hook=lex.CfnBot.LambdaCodeHookProperty(
                                    code_hook_interface_version="codeHookInterfaceVersion",
                                    lambda_arn="lambdaArn"
                                )
                            )
                        ),
                        locale_id="localeId"
                    )],
                    conversation_log_settings=lex.CfnBot.ConversationLogSettingsProperty(
                        audio_log_settings=[lex.CfnBot.AudioLogSettingProperty(
                            destination=lex.CfnBot.AudioLogDestinationProperty(
                                s3_bucket=lex.CfnBot.S3BucketLogDestinationProperty(
                                    log_prefix="logPrefix",
                                    s3_bucket_arn="s3BucketArn",

                                    # the properties below are optional
                                    kms_key_arn="kmsKeyArn"
                                )
                            ),
                            enabled=False
                        )],
                        text_log_settings=[lex.CfnBot.TextLogSettingProperty(
                            destination=lex.CfnBot.TextLogDestinationProperty(
                                cloud_watch=lex.CfnBot.CloudWatchLogGroupLogDestinationProperty(
                                    cloud_watch_log_group_arn="cloudWatchLogGroupArn",
                                    log_prefix="logPrefix"
                                )
                            ),
                            enabled=False
                        )]
                    ),
                    description="description",
                    sentiment_analysis_settings=sentiment_analysis_settings
                ),
                test_bot_alias_tags=[CfnTag(
                    key="key",
                    value="value"
                )]
                )
            """