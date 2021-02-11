from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from products.models import Products
import products.views

# Create your views here.
def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username):
                print('Username already taken')
                return redirect('register')
            elif User.objects.filter(email=email):
                print('Email already in use')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=firstname,last_name=lastname,username=username,email=email,password=password1)
                user.save()
                print('User Created')
                return redirect('login')
        else:
            print('Password didnt match')
            return redirect('register')
        return redirect('/products')

    else:
        return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            products = Products.objects.all()
            u = User.objects.get( username = username)
            print(u)

            return render(request,'index.html',{'products' : products,})
        else:
            print('invaliddd')
            return redirect('login')

    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')
