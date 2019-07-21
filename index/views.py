from django.shortcuts import render
from django.http import HttpResponse
from vendors.models import SeedsProduct

def index(request):
    return render(request, 'index.html')

def category(request):
    products=SeedsProduct.objects.all()
    context={
        "products":products
    }
    return render(request, 'category-full.html',context)

def equipments(request):
    return render(request, 'index/equipments.html')

