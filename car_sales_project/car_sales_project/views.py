from django.shortcuts import render
from cars.models import Car
from brand.models import brands

def home(request,brand_slug=None):
    data = Car.objects.all()
    if brand_slug is not None:
        brand = brands.objects.get(slug=brand_slug)
        data = Car.objects.filter(brand = brand)
    brand = brands.objects.all()
    return render(request,'index.html',{'cars': data , 'brands': brand})