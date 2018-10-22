from .models import Neighbourhood
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Neighbourhood,Profile,Business
from django.contrib.auth.models import User
class NewNeighbourhoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        exclude = []
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = []

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = []
class SignupForm(UserCreationForm):
 email = forms.EmailField()
 class Meta:
     model = User
     fields = ['username', 'email', 'password1', 'password2']