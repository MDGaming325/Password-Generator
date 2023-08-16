from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from password_generator.generator import gen_password
from .forms import RequestForm
from RequestsManagment.models import RequestModel


def main(request):

   
    generated_password = gen_password()
    
    ext_doc = loader.get_template('index.html')
    dict = {"generated_password": generated_password}

    x = ext_doc.render(dict)

    return HttpResponse(x)


def form(request):
     
    length = request.POST['length']
    symbols = request.POST['symbols']
    numbers = request.POST['numbers']

    RequestModel.objects.create(length=length, symbols=symbols, numbers=numbers)

   # x = {'form' : RequestForm()}

    # return render(request, "form.html", x)

class ScrapHtml:
    def __init__(self, length, symbols, numbers):
        self.length = length
        self.symbols = symbols
        self.numbers = numbers