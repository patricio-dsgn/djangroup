from django.shortcuts import render

# Create your views here.

# from django.http import HttpResponse
# def homePageView(request):
#     return HttpResponse("Hello, World!")

def home(request):
    return render(request,'store/home.html',{'nbar':'home'})

def about(request):
    return render(request,'store/about.html',{'nbar':'about'})

def products(request):
    return render(request,'store/products.html',{'nbar':'products'})

def services(request):
    return render(request,'store/services.html',{'nbar':'services'})

def contact(request):
    return render(request,'store/contact.html',{'nbar':'contact'})
