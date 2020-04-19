from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Produto


def index(request):
    prod = Produto.objects.all() #aqui o código busca todos os produtos cadastrados
    context = {
        "produtos": prod
    }
    return render(request, 'index.html', context)
def contato(request):
    return render(request, 'contato.html')


def produto(request, pk):
#    prod = Produto.objects.get(id=pk) #aqui o código busca o produto especifico clicado.
    prod = get_object_or_404(Produto, id=pk) #aqui o código busca o produto especifico clicado.

    context = {
        'produto': prod
    }
    return render(request, 'produto.html', context)