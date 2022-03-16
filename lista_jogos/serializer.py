from rest_framework import serializers
from lista_jogos.models import Jogo

class JogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jogo
        fields = '__all__'