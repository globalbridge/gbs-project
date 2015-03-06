from django import forms
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User

class MyRegistrationForm(forms.ModelForm):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password')

    def save(self, commit=True):
        user = super(MyRegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user