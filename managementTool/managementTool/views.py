from django.shortcuts import render
from django.template.response import TemplateResponse

def index(request):
    return TemplateResponse(request, 'index.html')


#fermeture de la session
#assistant.delete_session(assistant_id,  session["session_id"]).get_result()
