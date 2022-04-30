from django.shortcuts import render,redirect
from store.models import Vendor
from store.models import Client
from store.models import Post


from .forms import PostForm
from .forms import VendorForm
from django.utils import timezone

# def post_new(request):
#     form = PostForm()
#     return render(request, 'store/post_edit.html', {'form': form})
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('/post_list', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'store/post_create.html', {'form': form})

def post_all(request):
    query_post = Post.objects.all().order_by('-published_date')
    return render(request,'store/post_list.html',{'nbar':'post_list','query_post':query_post})

def vendor_new(request):
    if request.method == "POST":
        form = VendorForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('/vendors', pk=post.pk)
    else:
        form = VendorForm()
    return render(request, 'store/vendors_new.html', {'form': form})

def vendor_all(request):
    query_vendors = Vendor.objects.all().order_by('name')
    return render(request,'store/vendors.html',{'nbar':'vendors','query_vendors':query_vendors})

    
# Create hello world
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

def clients(request):
    query_results = Client.objects.all()
    return render(request,"store/clients.html",{'nbar':'clients', 'query_results':query_results})
    #return a response to your template and add query_results to the context








# def vendors(request):
#     query_vendors = Vendor.objects.all()
#     return render(request,'store/vendors.html',{'nbar':'vendors', 'query_vendors':query_vendors})


