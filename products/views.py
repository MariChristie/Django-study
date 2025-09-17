from django.shortcuts import render
from django.http import HttpResponse

def see_products(request):
    return HttpResponse("Here are the products.")