from django.contrib import admin
from django.urls import path, include
from vendors.views import index

urlpatterns = [
    path('farmers/', include("farmer.urls")),
    path('vendors/', include("vendors.urls")),
    path('index/', include("index.urls")),
    path('index/seeds', index, name="index"),
    path('admin/', admin.site.urls)
]
