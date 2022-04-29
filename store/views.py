from django.shortcuts import render,redirect
from store.models import Vendor
from store.models import Client

from .forms import PostForm, VendorForm

# def sign_in_vendors(request):
#     return render(request,'store/sign-in-vendors.html',{'nbar':'sign-in-vendors'})


def sign_in_vendors(request):
    if request.method == "POST":
        form = VendorForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # post.published_date = timezone.now()
            post.save()
            return redirect('vendors', pk=post.pk)
    else:
        form = VendorForm()
    return render(request, 'store/sign-in-vendors.html', {'form': form})

# Create your views here.
# def show(request):
#     clients = Client.objects.all()
#     return render(request,"show.html",{'client':clients})



def vendor_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # post.published_date = timezone.now()
            post.save()
            return redirect('vendors', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'store/register_vendor.html', {'form': form})

# def post(request):
#     return render(request,'store/post.html',{'nbar':'post'})


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


def contact(request):
    return render(request,'store/contact.html',{'nbar':'contact'})

def contact(request):
    return render(request,'store/contact.html',{'nbar':'contact'})






def show(request):
    query_results = Client.objects.all()
    return render(request,"store/clients.html",{'nbar':'clients', 'query_results':query_results})
    #return a response to your template and add query_results to the context

def vendors(request):
    query_vendors = Vendor.objects.all()
    return render(request,'store/vendors.html',{'nbar':'vendors', 'query_vendors':query_vendors})


