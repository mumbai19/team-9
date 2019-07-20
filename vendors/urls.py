
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('createSeed',views.createSeed, name="createSeed"),
    # path('seedDetails/<int:seed_id>',views.seedDetails, name="seedDetails")

]
