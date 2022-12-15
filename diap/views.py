from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from rest_framework import generics

from diap.models.person import Person


def index(request):
    return render(request, 'diap/index.html')


def tables(request):
    return render(request, 'diap/tables-basic.html')


def data_tables(request):
    persons = Person.objects.all()
    context = {
        'persons': persons
    }
    return render(request, 'diap/tables-data.html', context=context)


def show_person(request, person_id):
    return HttpResponse(f'Person_id={person_id}')


def pageNotFound(request, exception):
    return redirect('diap')
