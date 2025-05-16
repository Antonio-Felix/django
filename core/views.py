from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Filme

def lista_filmes(request):
    lista = Filme.objects.all().order_by('-id')
    paginator = Paginator(lista, 3)

    pagina = request.GET.get('page')
    filmes = paginator.get_page(pagina)

    return render(request, 'filmes/lista.html', {'filmes': filmes})
