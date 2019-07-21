from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('seeds/', views.category, name = 'category-seeds'),
    path('equipments/', views.equipments, name = 'category-equipments'),
    path('tutorial/', views.tutorial, name = 'tutorial'),
]