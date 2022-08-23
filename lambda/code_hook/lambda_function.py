"""
 This code sample demonstrates an implementation of the Lex Code Hook Interface
 in order to serve a bot which manages Insurance account services. Bot, Intent,
 and Slot models which are compatible with this sample can be found in the 
 Lex Console as part of the 'TelecomMobileServices' template.
"""

import time
import os
import logging
import dialogstate_utils as dialog
import fallback
import saludo
import otros_indicadores
import datos_indicador
import make_appointment

logger = logging.getLogger()
#logger.setLevel(logging.DEBUG)
    
# --- Main handler & Dispatch ---

def dispatch(intent_request):
    """
    Route to the respective intent module code
    """
    #print(intent_request)
    intent = dialog.get_intent(intent_request)
    intent_name = intent['name']
    active_contexts = dialog.get_active_contexts(intent_request)
    session_attributes = dialog.get_session_attributes(intent_request)
    number_of_attempts = dialog.get_session_attribute(intent_request, 'number_of_attempts') or '0'
    if number_of_attempts: number_of_attempts = int(number_of_attempts)
    
    
    # Default dialog state is set to delegate
    next_state = dialog.delegate(active_contexts, session_attributes, intent)

    
    
    
    # Dispatch to in-built Lex intents
    if intent_name == 'FallbackIntent':
        next_state = fallback.handler(intent_request)

    # Dispatch to in-built Lex intents
    if intent_name == 'SaludoIntent':
        next_state = saludo.handler(intent_request)


    # Dispatch to in-built Lex intents
    if intent_name == 'OtrosIndicadoresIntent':
        next_state = otros_indicadores.handler(intent_request)


    # Dispatch to in-built Lex intents
    if intent_name == 'DatosIndicador':
        next_state = datos_indicador.handler(intent_request)
    
    # Dispatch to the respective bot's intent handlers
    
    if intent_name == 'MakeAppointment':
        next_state = make_appointment.handler(intent_request)

    print (next_state)
    
    return next_state


def lambda_handler(event, context):
    """
    Route the incoming request based on intent.
    The JSON body of the request is provided in the event slot.
    """
    # By default, treat the user request as coming from the America/New_York time zone.
    os.environ['TZ'] = 'America/New_York'
    time.tzset()
    print('event: ', event)

    return dispatch(event)
