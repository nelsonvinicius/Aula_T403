from django.shortcuts import render
from website.models import Pessoa

# Create your views here.

def index(request):
    contexto = {}
    if request.method == 'POST':
        pessoa = Pessoa()
        pessoa.nome = request.POST.get('nome')
        pessoa.sobrenome = request.POST.get('sobrenome')
        pessoa.email = request.POST.get('email')
        pessoa.genero = request.POST.get('genero')
        pessoa.biografia = request.POST.get('biografia')
        pessoa.save()
        contexto = {'msg': 'Parabéns :)'}

    return render(request, 'index.html', contexto)


def sobre(request):
    pessoa = Pessoa.objects.filter()
    contexto = {
        'pessoas':pessoa
    }
    return render(request, 'sobre.html', contexto)