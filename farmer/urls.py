from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('market', views.getMarket, name="market"),
    path('<int:product_id>', views.getDetails, name="details"),
    path('createFish', views.createFish, name= "createFish"),
    path('help',views.getHelp,name="help")
]
