from django.shortcuts import render


def home2(request):
    return render(request,'memapp/home.html')
