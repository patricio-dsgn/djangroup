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



from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user


