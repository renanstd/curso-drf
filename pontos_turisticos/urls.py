from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from core.api.viewsets import PontoTuristicoViewSet
from atracoes.api.viewsets import AtracoesViewSet
from enderecos.api.viewsets import EnderecosViewSet
from comentarios.api.viewsets import ComentariosViewSet
from avaliacoes.api.viewsets import AvaliacoesViewSet


router = routers.DefaultRouter()
router.register(r'pontoturistico', PontoTuristicoViewSet, basename='PontoTuristico')
router.register(r'atracoes', AtracoesViewSet)
router.register(r'enderecos', EnderecosViewSet)
router.register(r'comentarios', ComentariosViewSet)
router.register(r'avaliacoes', AvaliacoesViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
