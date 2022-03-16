from re import search
from django.contrib import admin
from lista_jogos.models import Jogo

class Jogos(admin.ModelAdmin):
    list_display = ('id', 'nome','categoria', 'plataformas','modo_de_jogo','sinopse', 'data_lancamento')
    list_display_links = ('id', 'nome')
    search_field = ('nome',)
    list_per_page = 20
admin.site.register(Jogo, Jogos)