from django.shortcuts import render

# Create your views here.

# from django.http import HttpResponse
# def homePageView(request):
#     return HttpResponse("Hello, World!")

def home(request):
    return render(request,'store/home.html')

def about(request):
    return render(request,'store/about.html')

def products(request):
    return render(request,'store/products.html')

def services(request):
    return render(request,'store/services.html')

def contact(request):
    return render(request,'store/contact.html')
