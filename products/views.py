from django.shortcuts import render, redirect
from .models import People

def see_products(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')

        person = People(name=name, age=age)
        person.save()

        return redirect('see_products')

    all_people = People.objects.all()
    context = {'People': all_people}
    return render(request, 'products/see_products.html', context)

def insert_product(request):
    return render(request, 'products/insert_product.html')