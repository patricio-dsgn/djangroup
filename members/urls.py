from django.urls import path
from . import views

urlpatterns = [
    path('login_user', views.login_user, name='login'),
    path('log_out', views.logout_user, name='logout'),
    # path('users/', include('django.contrib.auth.urls')),
    # path('users/', include('users.urls')),
]