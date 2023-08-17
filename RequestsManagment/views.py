from django.shortcuts import render
from RequestsManagment.models import RequestModel
from RequestsManagment.forms import RequestForm
from password_generator.generator import gen_password

def form(request):
    length_REQ = int(request.GET.get('length', 0))
    symbols_REQ = bool(request.GET.get('symbols', False))
    numbers_REQ = bool(request.GET.get('numbers', False))
    
    RequestModel.objects.create(length=length_REQ, symbols=symbols_REQ, numbers=numbers_REQ)
    
    x = {'form': RequestForm()}

    return render(request, "form.html", x)

