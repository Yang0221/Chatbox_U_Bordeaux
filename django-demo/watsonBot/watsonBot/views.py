from django.shortcuts import render
from django.template.response import TemplateResponse
import json
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from django.http import Http404, HttpResponse

#mettre les clés dans des variables
assistant_id = "27d22841-06bc-46ed-9343-9c840acf00f0"
api_key = 'EvR0NbioVwRGtvL1qZlFJlcXuGPH9_YCzyeAES2AIb8k'
#assistant_id = "f7a3b52e-4d7e-412e-9143-b0ea96776d46"
#api_key = 'eXD4siVcZGXJMYtddtfMkmzaaIZe2vcrbbya9BRC4kdR'

authenticator = IAMAuthenticator(api_key)
assistant = AssistantV2(
    version='2019-02-28',
    authenticator=authenticator)
assistant.set_service_url('https://api.eu-de.assistant.watson.cloud.ibm.com')
#assistant.set_service_url('https://gateway-fra.watsonplatform.net/assistant/api')

#création d'une session
session = assistant.create_session(assistant_id).get_result()

def new_message(request):
    if request.is_ajax and request.POST:

        #récupération du message
        message = assistant.message(
            assistant_id,
            session["session_id"],
            input={'text': request.POST.get('text')}).get_result()
        print(message)

        #préparation du texte à envoyer
        if message['output']['generic'][0]['response_type'] == 'option':
            response = {
            'title': message['output']['generic'][0]['title'],
            'options' : message['output']['generic'][0]['options']
            }
        if message['output']['generic'][0]['response_type'] == 'text':
             response = {
             'text': message['output']['generic'][0]['text']
        }

        return HttpResponse(json.dumps(response), content_type="application/json")
    else:
        raise Http404


def index(request):
    message = assistant.message(assistant_id,session["session_id"]).get_result()
    return TemplateResponse(request, 'index.html', {'text' : message['output']['generic'][0]['text']})


#fermeture de la session
#assistant.delete_session(assistant_id,  session["session_id"]).get_result()