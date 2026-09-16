from django.db import models

'''Cada model é uma classe Python que vira uma tabela no banco. Cada atributo da classe vira uma coluna. Você
descreve os dados uma vez e o Django cuida do resto.
'''

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    ano = models.IntegerField()
    disponivel = models.BooleanField(default=True)

    def __str__(self):  #Define como o objeto aparece escrito — aqui, pelo título. Ajuda muito no Admin e no shell.

        return self.titulo