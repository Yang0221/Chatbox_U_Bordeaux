import json
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('EvR0NbioVwRGtvL1qZlFJlcXuGPH9_YCzyeAES2AIb8k')
#authenticator = IAMAuthenticator('eXD4siVcZGXJMYtddtfMkmzaaIZe2vcrbbya9BRC4kdR')
assistant = AssistantV2(
    version='2019-02-28',
    authenticator=authenticator)

assistant.set_service_url('https://api.eu-de.assistant.watson.cloud.ibm.com')
#assistant.set_service_url('https://gateway-fra.watsonplatform.net/assistant/api')

#########################
# Sessions
#########################

session = assistant.create_session("27d22841-06bc-46ed-9343-9c840acf00f0").get_result()
#session = assistant.create_session("f7a3b52e-4d7e-412e-9143-b0ea96776d46").get_result()
print(json.dumps(session, indent=2))

#########################
# Message
#########################

message = assistant.message(
    "27d22841-06bc-46ed-9343-9c840acf00f0",
    #"f7a3b52e-4d7e-412e-9143-b0ea96776d46",
    session["session_id"],
    input={'text': 'mdp'},
    context={
        'metadata': {
            'deployment': 'myDeployment'
        }
    }).get_result()
    
print(json.dumps(message, indent=2))
#print(message['output']['generic'][0]['title'])
c = {
'title': message['output']['generic'][0]['title']
}
for x in range(0, 1):
    c['options'][0] = message['output']['generic'][0]['options'][x]['label']
    c['options'][x]['text'] = message['output']['generic'][0]['text'][0]['value']['input']['text']
print(c)

assistant.delete_session("27d22841-06bc-46ed-9343-9c840acf00f0",  session["session_id"]).get_result()
#assistant.delete_session("f7a3b52e-4d7e-412e-9143-b0ea96776d46",  session["session_id"]).get_result()
