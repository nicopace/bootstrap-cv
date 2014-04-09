from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Curriculum

# Create your views here.

def view_cv(request, nombre_completo):
    nombre, apellido = nombre_completo.split(' ', 1)

    cvs = Curriculum.objects.filter(name=nombre, surname=apellido)
    cv = cvs[0]

    return render_to_response('cv.html',
                              {'cv': cv},
                              context_instance=RequestContext(request)
                              )
