from django.urls import path
from teacher.views import CadastrarAulaAPIView

urlpatterns = [
    path('', CadastrarAulaAPIView.as_view()),
]