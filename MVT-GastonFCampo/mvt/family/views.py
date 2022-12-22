from django.shortcuts import render
from django.http import HttpResponse
from family.models import Family

def create_family(request):
    Family.objects.create(name = 'Juan', age = 20, study = True)
    Family.objects.create(name = 'Pepe', age = 21, study = True)
    Family.objects.create(name = 'Martin', age = 22, study = False)
    return HttpResponse('Los datos de la familia fueron creados. <br><br>Ingresa a: <a>http://127.0.0.1:8000/list-family/</a> para ver los datos de los familiares.')

def list_family(request):
    all_family = Family.objects.all()
    context = {
        'family' : all_family,
    }
    return render(request, 'list-family.html', context)
