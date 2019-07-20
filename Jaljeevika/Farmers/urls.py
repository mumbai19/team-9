from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('market',views.market , name = "market"),
    
]
