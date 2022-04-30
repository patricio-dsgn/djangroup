from django.urls import path

from django.contrib import admin
from store import views


# from .views import homePageView
# urlpatterns = [
#     path("", homePageView, name="home"),
# ]


from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.home),
    path('about', views.about),
    path('products', views.products),
    path('services', views.services),
    path('contact', views.contact),
    path('clients',views.show),
    
    path('post_create',views.post_new),
    path('post_list',views.post_all),

    path('vendors',views.vendors),
    path('sign-in-vendors',views.sign_in_vendors),

    # path('sign-in-vendors',views.sign_in_vendors),
]