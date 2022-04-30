from django import forms

from .models import Post, Vendor

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)


class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ('run', 'name', 'phone', 'email')


