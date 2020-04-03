import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import AssistantV2


session_id = "00"
authenticator = IAMAuthenticator('EvR0NbioVwRGtvL1qZlFJlcXuGPH9_YCzyeAES2AIb8k') #Mettre la première clef ici (EvR0NbioVwRGtvL1qZlFJlcXuGPH9_YCzyeAES2AIb8k)
assistant = AssistantV2(
    version='2019-09-12',
    authenticator=authenticator
)

clef2 = "37560d5c-c606-499e-b779-599ff5bc30a2" #mettre la 2nd clef ici (37560d5c-c606-499e-b779-599ff5bc30a2)

'''Possiblement possible de se connecter à une BDD via : https://cloud.ibm.com/docs/assistant?topic=assistant-dialog-webhooks'''

def connect():
    global session_id, assistant
    assistant.set_service_url('https://api.eu-de.assistant.watson.cloud.ibm.com')
    session_id = assistant.create_session(clef2).get_result()["session_id"]

def disconnect():
    global session_id, assistant
    assistant.delete_session(clef2, session_id).get_result()

#########################
# Message
#########################

def bot_message(input_msg):
    global session_id, assistant
    message = assistant.message(
        clef2,
        session_id,
        input={'text' : input_msg},          ## de la forme "input = {'text' : 'msg'}"
        context={
            'metadata': {
                'deployment': 'myDeployment'
            }
    }).get_result()
    #print()
    #print(message["output"]["generic"]) ## Liste de réponse (type et options)
    #print()
    #print(json.dumps(message, indent=2))
    return message["output"]["generic"]
