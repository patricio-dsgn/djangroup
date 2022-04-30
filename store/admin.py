from django.contrib import admin

# Register your models here.
from . models import Student,Client,Post,Vendor
admin.site.register(Student)
admin.site.register(Client)
admin.site.register(Post)
admin.site.register(Vendor)