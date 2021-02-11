from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Products
from django.contrib.auth.models import User,auth
# Create your views here.

def index(request):
    products = Products.objects.all()
    return render(request,'index.html',{'products' : products})

def new(request):
    return HttpResponse('New Products')

def search(request):
    flag = 0
    if request.method == 'POST' and request.POST['val1'] != '':
        val1 = request.POST['val1']
        products = Products.objects.all()
        for product in products:
            if val1.lower() == product.name.lower():
                flag = 1
                break
        if flag == 1:
            return render(request,'search.html',{'product':product})
        else:
             return HttpResponse('No Match Found')
    return HttpResponse('Empty Search')

def add(request):
    if request.method == 'POST':
        products = Products.objects.all()
        
        val = int(request.POST['productid'])
        for product in products:
            if val == product.id:
                print('true', product.name)
                product.inCart = True
                product.save()
        return render(request, 'add.html')
    return render(request,'add.html')

def cart(request):
    products = Products.objects.all()
    return render(request,'cart.html', {'products': products})

def cont(request):
    return redirect('index')

