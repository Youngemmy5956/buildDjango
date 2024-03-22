from django.shortcuts import render

# Create your views here.
from http.client import HTTPResponse
from django.http import HttpResponse
from datetime import datetime
# from .models import product


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

def foods(request, food_name):
    food = {
        'pizza' : 'type of fast food',
        'burger' : 'type of fast food',
        'pasta': 'type of italian food'
    }
    choice_of_food = food[food_name]
    return HttpResponse(f"<h2>{food_name}</h2> " + choice_of_food)


def home(request):
    return HttpResponse("Welcome to Little Lemon !")

def about(request):
    return HttpResponse("About us")

def menu(request):
    return HttpResponse("Menu for Little Lemon")

def book(request):
    return HttpResponse("Make a booking")

def my_view(request): 
    # ... 
    if condition==True: 
        return HttpResponseNotFound('<h1>Page not found</h1>') 
    else: 
        return HttpResponse('<h1>Page was found</h1>') 
    
    # def my_view(request): 
    # # ... 
    # if condition==True: 
    #     return HttpResponse('<h1>Page not found</h1>', status_code='404') 
    # else: 
    #     return HttpResponse('<h1>Page was found</h1>') 


def detail(request, id): 
    try: 
        p = Product.objects.get(pk=id) 
    except Product.DoesNotExist: 
        raise Http404("Product does not exist") 
    return HttpResponse("Product Found") 


# def myview(request):   
#     if request.method == "POST":   
#         form = MyForm(request.POST)   
#         if form.is_valid():   
#             #process the form data 
#         else:   
#                 return HttpResponse("Form submitted with invalid data") 
