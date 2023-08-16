from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from password_generator.generator import gen_password



def main(request):

    generated_password = gen_password()
    
    ext_doc = loader.get_template('index.html')
    dict = {"generated_password": generated_password}

    x = ext_doc.render(dict)

    

    return HttpResponse(x)


def form(request):
    return render(request, "form.html")