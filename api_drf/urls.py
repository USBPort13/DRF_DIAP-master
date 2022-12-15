from django.urls import path

from api_drf.views import PersonAPIView


urlpatterns = [
    path('api/v1/personlist/', PersonAPIView.as_view()),
]
