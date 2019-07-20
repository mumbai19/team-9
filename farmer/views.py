from django.shortcuts import render
from .models import Fish
from vendors.models import SeedsProduct

# Create your views here.
def createFish(request):
    if request.method == "POST":
        fishType = request.POST['fish_type']
        quantity = request.POST['quantity']
        price = request.POST['price']


        fish = Fish(fishType=fishType,quantity=quantity,price=price)
        fish.save()

    return render("farmers/createFish")

def getMarket(request):
    products = SeedsProduct.objects.all()
    return render(request,"farmers/market.html",{"products":products})


def getDetails(request):
    return render(request,"farmers/details.html")
# def search(request):
#     productType = request.GET['type']

#     if(productType == "seed"):
#         products = Seeds.objects.filter(location = "")


#     context = {
#         products : products
#     }
#     return render("marketProducts",context)


# def productDetails(request,productType,product_id):
#     return "details"     


