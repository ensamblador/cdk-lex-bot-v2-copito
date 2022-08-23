import dialogstate_utils as dialog
def handler(intent_request):
    intent = dialog.get_intent(intent_request)
    active_contexts = dialog.get_active_contexts(intent_request)
    session_attributes = dialog.get_session_attributes(intent_request)
    default_fallback_message = "Hola Soy Kopito, el de los otros indicadores. Elije: \n 1. Valor UTM \n 2. Valor IMACEC, \n 3. Valor IPC"
    message = default_fallback_message
    return dialog.elicit_intent(
        active_contexts, session_attributes, intent, 
        [{'contentType': 'PlainText', 'content': message}])
    