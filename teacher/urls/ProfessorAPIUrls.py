from django.urls import path
from teacher.views import ProfessorAPIView

urlpatterns = [
    path('', ProfessorAPIView.as_view()),
]