from django.shortcuts import render
from RequestsManagment.models import RequestModel
from RequestsManagment.forms import RequestForm
from password_generator.algorithms import gen_password


def main(request):
    length_REQ = int(request.GET.get('length', 0))
    symbols_REQ = bool(request.GET.get('symbols', False))
    numbers_REQ = bool(request.GET.get('numbers', False))

    '''
    # Future feature
    RequestModel.objects.create(length=length_REQ, symbols=symbols_REQ, numbers=numbers_REQ)
    '''

    generated_password = gen_password(length_REQ, symbols_REQ, numbers_REQ)

    dict = {'form': RequestForm(), 'generated_password': generated_password}

    return render(request, "form.html", dict)
