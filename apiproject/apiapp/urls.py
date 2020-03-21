from django.urls import path
from .views import *
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

urlpatterns = [
    path('jogo/', JogoView.as_view()),
    path('jogo/<int:pk>/', JogoViewDetails.as_view()),
    path('gettoken/', obtain_jwt_token),
    path('refreshtoken/', refresh_jwt_token)
]