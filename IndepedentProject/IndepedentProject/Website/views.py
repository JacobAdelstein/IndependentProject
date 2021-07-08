from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('<H1> Home Page <H1>')

def about(request):
    return HttpResponse('<p> Meteor Prototypes<p>')