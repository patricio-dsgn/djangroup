from django.urls import path
# from .views import homePageView

# urlpatterns = [
#     path("", homePageView, name="home"),
# ]

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.home2),
]