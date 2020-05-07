from django.shortcuts import render
from django.template.response import TemplateResponse
import json
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from django.http import Http404, HttpResponse
from localisation.models import Building
from localisation.models import Room
from localisation.models import Campus
from localisation.models import SynonymBuilding
from localisation.models import SynonymRoom
from localisation.models import SynonymCampus

#mettre les clés dans des variables
assistant_id = "37560d5c-c606-499e-b779-599ff5bc30a2"
api_key = 'EvR0NbioVwRGtvL1qZlFJlcXuGPH9_YCzyeAES2AIb8k'


authenticator = IAMAuthenticator(api_key)
assistant = AssistantV2(
    version='2019-02-28',
    authenticator=authenticator)
assistant.set_service_url('https://api.eu-de.assistant.watson.cloud.ibm.com')

#création d'une session
session = assistant.create_session(assistant_id).get_result()

def new_message(request):
    if request.is_ajax and request.POST:
        #récupération du message
        message = assistant.message(
            assistant_id,
            session["session_id"],
            input = {
                'message_type' : 'text',
                'text' : request.POST.get('text'),
                'options' : {"return_context" : True}}
            ).get_result()

        address = ""
        lat = 0.0
        long = 0.0

        if message['context']['skills']['main skill']['user_defined']['objective'] != 'N/A' :
            item = message["context"]["skills"]["main skill"]["user_defined"]['objective']
            object = None
            try:
                object = Campus.objects.get(name = item)
            except Campus.DoesNotExist:
                try:
                    object = SynonymCampus.objects.get(value = item).id_campus
                #ce n'est pas un campus
                except SynonymCampus.DoesNotExist:
                    try:
                        object = Building.objects.get(name = item)
                    except Building.DoesNotExist:
                        try:
                            object = SynonymBuilding.objects.get(value = item).id_building
                        #ce n'est pas un building
                        except SynonymBuilding.DoesNotExist:
                            try:
                                object = Room.objects.get(name = item)
                                object = Building.objects.get(id = object.id_building)
                            except Room.DoesNotExist:
                                object = SynonymRoom.objects.get(value = item).id_room
                                object = Room.objects.get(id = object)
                                object = Building.objects.get(id = object.id_building)
            if object != None:
                address = object.address
                tmp = object.coordinates.split("/")
                lat = tmp[0]
                long = tmp[1]



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
        response['address'] = address
        response['lat'] = lat
        response['long'] = long

        return HttpResponse(json.dumps(response), content_type="application/json")
    else:
        raise Http404


def main(request):
    message = assistant.message(assistant_id,session["session_id"]).get_result()
    return TemplateResponse(request, 'chatbot.html', {'text' : message['output']['generic'][0]['text']})


#fermeture de la session
#assistant.delete_session(assistant_id,  session["session_id"]).get_result()
