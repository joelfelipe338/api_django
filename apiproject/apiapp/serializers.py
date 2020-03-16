from rest_framework import serializers
from .models import *
class JogoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Jogo
        fields = "__all__"

