from django.db import models

class Jogo(models.Model):
    nome = models.CharField(max_length=30)
    categoria = models.CharField(max_length=50)
    modo_de_jogo = models.CharField(max_length=50)
    plataformas = models.CharField(max_length=50)
    sinopse = models.TextField()
    data_lancamento = models.DateField()

    def __str__(self):
        return self.nome
