from django import forms
from .models import ContactMessage
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    def save(self):
        ContactMessage.objects.create(
            name=self.cleaned_data['name'],
            email=self.cleaned_data['email'],
            message=self.cleaned_data['message']
        )
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Signup Form
class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
