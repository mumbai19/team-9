from django.shortcuts import render
from vendors.models import SeedsProduct
from farmer.models import Fish

def index(request):
    return render(request, 'index.html')

def category(request):
    products=SeedsProduct.objects.all()
    context={
        "products":products
    }
    return render(request, 'category-full.html',context)

def equipments(request):
    return render(request, 'equipments.html')

def tutorial(request):
    return render(request, 'tutorials.html')

def category1(request):
    products = Fish.objects.all()
    context = {
        "products": products
    }
    return render(request, 'category.html', context)