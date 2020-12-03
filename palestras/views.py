from rest_framework import viewsets, generics
from palestras.models import Palestra, Ouvinte, Inscricao
from palestras.Serializer import PalestraSerializer, OuvinteSerializer, InscricaoSerializer, ListaInscricoesOuvinteSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from django.http import JsonResponse

# Create your views here.
class PalestrasViewSet(viewsets.ModelViewSet):
    """Exibindo todos as palestras"""
    queryset = Palestra.objects.all()
    serializer_class = PalestraSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]



class OuvintesViewSet(viewsets.ModelViewSet):
    """Exibindo todos os ouvintes inscritos"""
    queryset = Ouvinte.objects.all()
    serializer_class = OuvinteSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]



class InscricaoViewSet(viewsets.ModelViewSet):
    """Exibindo todas as inscrições"""
    queryset = Inscricao.objects.all()
    serializer_class = InscricaoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]



class ListaInscricoesOuvinteViewSet(generics.ListAPIView):
    """Exibindo as inscricoes de um ouvinte"""
    def get_queryset(self):
        queryset = Inscricao.objects.filter(ouvintefk=self.kwargs['pk'])
        return queryset
    serializer_class = ListaInscricoesOuvinteSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]