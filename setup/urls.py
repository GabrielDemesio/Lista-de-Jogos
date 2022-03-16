from email.mime import base
from posixpath import basename
from django.contrib import admin
from django.urls import path, include
from lista_jogos.views import JogoViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('jogos', JogoViewset, basename='Jogos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

