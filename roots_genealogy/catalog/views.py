from django.shortcuts import render
from catalog.models import Produse

def produse_index(request):
    produse = Produse.objects.all()
    context = {
        'produse':produse
    }
    return render(request, 'produse_index.html', context)

def produse_detail(request, pk):
    produs = Produse.objects.get(pk=pk)
    context = {
        'produs':produs
    }
    return render(request, 'produse_detail.html', context)
