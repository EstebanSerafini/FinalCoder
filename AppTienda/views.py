from django.shortcuts import render
from .models import Producto

def tienda(request):
    
    productos = Producto.objects.all()
    
    return render(request, "AppTienda/tienda.html", {"productos":productos})

