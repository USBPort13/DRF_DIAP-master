from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='diap'),
    path('tables/', tables, name='tables'),
    path('data_tables/', data_tables, name='data_tables'),
    path('person/<int:person_id>/', show_person, name='person'),
]

