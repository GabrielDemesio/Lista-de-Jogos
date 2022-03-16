from rest_framework import viewsets
from lista_jogos.models import Jogo
from lista_jogos.serializer import JogoSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class JogoViewset(viewsets.ModelViewSet):
    """"Exibindo todos os jogos!"""
    queryset = Jogo.objects.all()
    serializer_class = JogoSerializer
    authencation_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]