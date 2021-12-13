from django.http import HttpResponse
from django.shortcuts import render
from django.http import request
from store.models import Product

def Home(request):
    products = Product.objects.filter(is_available=True)
    context = {
        'products': products
    }
    return render(request, 'home.html', context)