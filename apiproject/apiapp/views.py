from rest_framework import generics
from .serializers import *
from .models import *
# Create your views here.

class JogoView(generics.ListCreateAPIView):
    queryset = Jogo.objects.all()
    serializer_class = JogoSerializer


class JogoViewDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Jogo.objects.all()
    serializer_class = JogoSerializer


