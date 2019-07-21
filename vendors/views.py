from django.shortcuts import render, redirect, HttpResponse
from . models import SeedsProduct
# Create your views here.
def index(request):
    products = SeedsProduct.objects.filter(vendor_name='saket')
    # return HttpResponse(products)
    # print(products)
    return render(request,"../index/templates/category-full.html",{"products":products})

def createSeed(request):
    if(request.method=='POST'):
        v_name=request.POST.get('v_name')
        seed_name=request.POST.get('seed')
        exweather=request.POST.get('exweather')
        exph=request.POST.get('exph')
        price=request.POST.get('price')
        list1 = SeedsProduct(
                    vendor_name  = "saket",
                    seed_name = seed_name,
                    exweather = exweather,
                    exph = exph,
                    price = price
                )
        list1.save()
        return redirect('/vendors/')
    return render(request,"vendors/createSeed.html")


# def seedDetails(request,seed_id):
    seedDetails = SeedsProduct.objects.filter(id = seed_id)
    return render(request,"vendors/details",{"details":seedDetails})