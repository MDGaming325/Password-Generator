from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from password_generator.generator import gen_password
from .forms import RequestForm
from RequestsManagment.models import RequestModel


def main(request):

   
    generated_password = ""
    
    ext_doc = loader.get_template('index.html')
    dict = {"generated_password": generated_password}

    x = ext_doc.render(dict)

    return HttpResponse(x)


