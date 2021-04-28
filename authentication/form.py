from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomCreationForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter Username"}
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter Email"}
        )
    )
    password1 = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "password",
                "class": "form-control",
                "placeholder": "Enter Password",
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "password",
                "class": "form-control",
                "placeholder": "Confirm Password",
            }
        )
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2",]
