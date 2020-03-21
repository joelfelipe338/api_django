from rest_framework import generics
from .serializers import *
from .models import *
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class JogoView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Jogo.objects.all()
    serializer_class = JogoSerializer


class JogoViewDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Jogo.objects.all()
    serializer_class = JogoSerializer

