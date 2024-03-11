from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from datetime import datetime

def home(request):
    return HttpResponse("Welcome to little lemon restaurant!")

def display_date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))


