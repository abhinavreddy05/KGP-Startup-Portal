from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser, StartupModel, MentorModel


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("email",)

class StartupForm(forms.ModelForm):
    class Meta:
        model = StartupModel
        fields = '__all__'
        exclude = ['user', 'verified']

class MentorForm(forms.ModelForm):
    class Meta:
        model = MentorModel
        fields = '__all__'
        exclude = ['user', 'verified']