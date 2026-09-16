

'''A view é uma função que recebe a requisição e devolve uma resposta. O arquivo acervo/urls.py diz qual endereço chama
essa função — mas ele NÃO vem pronto: o comando startapp não cria esse arquivo. Você precisa criá-lo manualmente
dentro da pasta do app. Nas próximas aulas trocamos o texto por templates'''

from django.shortcuts import render, redirect
from .models import Livro
from .forms import LivroForm

def lista_livros(request):
    livros = Livro.objects.all() # busca no banco
    return render(
        request, 'acervo/lista.html',
        {'livros': livros} # envia ao template
)

def novo_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save() # grava no banco
        return redirect('lista')
    else:
        form = LivroForm()
    return render(request, 'acervo/form.html', {'form': form})


