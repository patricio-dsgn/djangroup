from django.shortcuts import render,redirect


# Create your views here.


# def show(request):
#     clients = Client.objects.all()
#     return render(request,"show.html",{'client':clients})

from store.models import Client
def show(request):
    query_results = Client.objects.all()
    return render(request,"store/show.html",{'query_results__':query_results})
    #return a response to your template and add query_results to the context


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

