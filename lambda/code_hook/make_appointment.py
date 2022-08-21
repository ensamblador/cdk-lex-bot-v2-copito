import dialogstate_utils as dialog
from datetime import date
import re
from prompts_responses import Prompts, Responses

def fulfillment(intent_request, intent, active_contexts, session_attributes):
    print ('Fullfillment!')
    intent = dialog.get_intent(intent_request)
    active_contexts = dialog.get_active_contexts(intent_request)
    session_attributes = dialog.get_session_attributes(intent_request)
    dialog.set_session_attribute(intent_request, 'number_of_attempts', '0')
    responses = Responses('make_appointment')
    
    appointment_type = dialog.get_slot('AppointmentType', intent)
    appointment_date = dialog.get_slot('Date', intent)
    appointment_time = dialog.get_slot('Time', intent)
    
    response = responses.get('Response',appointment_type=appointment_type, appointment_date=appointment_date, appointment_time=appointment_time)
    
    return dialog.elicit_intent(
                active_contexts, session_attributes, intent, 
                [{'contentType': 'PlainText', 'content': response}])


    

def handler(intent_request):
    content_type =  'PlainText'
    prompts = Prompts('make_appointment')

    intent = dialog.get_intent(intent_request)
    active_contexts = dialog.get_active_contexts(intent_request)
    session_attributes = dialog.get_session_attributes(intent_request)
    

    appointment_type = dialog.get_slot('AppointmentType', intent)
    appointment_date = dialog.get_slot('Date', intent)
    appointment_time = dialog.get_slot('Time', intent)
    
    if not appointment_type:
        prompt = prompts.get('AppointmentType')
        return dialog.elicit_slot(
            'AppointmentType', active_contexts,
            session_attributes, intent,
            [{'contentType': 'PlainText', 'content': prompt}])    
                
    if not appointment_date:
        prompt = prompts.get('Date')
        return dialog.elicit_slot(
            'Date', active_contexts,
            session_attributes, intent,
            [{'contentType': 'PlainText', 'content': prompt}]) 
            
    if not appointment_time:
        prompt = prompts.get('Time')
        return dialog.elicit_slot(
            'Time', active_contexts,
            session_attributes, intent,
            [{'contentType': 'PlainText', 'content': prompt}]) 
                
                

    
    print ('appointment_type:', appointment_type)
    print ('appointment_date:', appointment_date)
    print ('appointment_time:', appointment_time)
    
    

    if intent['confirmationState'] == 'Confirmed':
        return fulfillment(
            intent_request, intent, active_contexts, session_attributes)
    

    return fulfillment(
            intent_request, intent, active_contexts, session_attributes)
            
    return dialog.delegate(active_contexts, session_attributes, intent)