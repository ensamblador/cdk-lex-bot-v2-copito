import dialogstate_utils as dialog
import requests
import json



def request(indicador, fecha): 
    ind = 'dolar'

    if indicador == 'UF': 
        ind =  'uf'
    if indicador == 'UTM':
        ind = 'utm'
    if indicador == 'IMACEC':
        ind = 'imacec' 
    if indicador == 'IPC':
        ind = 'ipc' 
    
    fecha_parts = fecha.split('-')
    fecha_a = fecha_parts[0]
    fecha_m = fecha_parts[1]
    fecha_d = fecha_parts[2]
    
    requested_url = f'https://mindicador.cl/api/{ind}/{fecha_d}-{fecha_m}-{fecha_a}'
    #response = requests.request("GET", requested_url)
    #print (response.text)
    #valor =  json.loads(response.text)['serie'][0]['valor']
    valor = 100
    return valor


def handler(intent_request):
    intent = dialog.get_intent(intent_request)
    active_contexts = dialog.get_active_contexts(intent_request)
    session_attributes = dialog.get_session_attributes(intent_request)
    
    indicador = dialog.get_slot('IndicadorName', intent)
    Rut = dialog.get_slot('Rut', intent)
    Date = dialog.get_slot('Fecha', intent)
    

    
    
    if intent['state'] == "ReadyForFulfillment":
        valor_indicador = request(indicador, Date)
        message = f"El valor del {indicador} el día {Date} es ${valor_indicador}. Consultado por {Rut}, algo más?"
        return dialog.close(active_contexts, session_attributes, intent,  [{'contentType': 'PlainText', 'content': message}])
        
    return dialog.delegate(active_contexts, session_attributes, intent)

    

    