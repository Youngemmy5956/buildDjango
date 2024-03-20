from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
     path('drinks/<str:drink_name>', views.drinks, name="drink_name"), 
     path('date', views.display_date),
     path('foods/<str:food_name>', views.foods, name="food_name")
     
]
