from django.shortcuts import render
from django.http import HttpResponse

def see_products(request):
    return render(request, 'products/see_products.html')

def inser_product(request):
    return HttpResponse("Insert a new product here.")

