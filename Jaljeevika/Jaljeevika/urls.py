
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('farmers/', include("Farmers.urls")),
    path('admin/', admin.site.urls),
]
