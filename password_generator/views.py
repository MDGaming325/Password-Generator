from django.http import HttpResponse
from django.template import Template, loader
import datetime



def main(request):

    date = datetime.datetime.now()
    
    ext_doc = loader.get_template('index.html')
    dict = {"time": date}

    x = ext_doc.render(dict)

    

    return HttpResponse(x)