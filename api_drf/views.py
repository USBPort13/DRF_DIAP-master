from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from api_drf.serializers import PersonSerializer
from diap.models.person import Person


class PersonAPIView(generics.ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer