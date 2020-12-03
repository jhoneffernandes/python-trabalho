from rest_framework import serializers
from palestras.models import Palestra, Ouvinte, Inscricao


class PalestraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Palestra
        fields = ['id', 'title', 'local', 'datetimeStart', 'datetitmeEnd']



class OuvinteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ouvinte
        fields = '__all__'



class InscricaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscricao
        fields = ['id', 'palestrafk', 'ouvintefk']



class ListaInscricoesOuvinteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscricao
        fields = ['palestrafk']