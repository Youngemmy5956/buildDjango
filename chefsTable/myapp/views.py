from django.shortcuts import render

# Create your views here.
from http.client import HTTPResponse
from django.http import HttpResponse
from datetime import datetime

def home(request):
    return HttpResponse("Welcome to little lemon restaurant!")

def display_date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))


def drinks(request, drink_name):
    drink = {
        'mocha' : 'type of coffee',
        'tea' : 'type of hot beverage',
        'lemonade': 'type of refreshment'
    }
    choice_of_drink = drink[drink_name]
    return HttpResponse(f"<h2>{drink_name}</h2> " + choice_of_drink)