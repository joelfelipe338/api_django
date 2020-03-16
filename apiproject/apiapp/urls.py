from django.urls import  path
from .views import *

urlpatterns = [
    path('jogo/', JogoView.as_view()),
    path('jogo/<int:pk>/', JogoViewDetails.as_view())
]