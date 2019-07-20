from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('farmers/', include("farmer.urls")),
    path('vendors/', include("vendors.urls")),
    path('admin/', admin.site.urls)
]
