from django.shortcuts import render
from AppServicios.models import Servicio   

# Create your views here.

def servicios(request):
    servicios = Servicio.objects.all()
    return render(request, "AppServicios/servicios.html", {"servicios": servicios})