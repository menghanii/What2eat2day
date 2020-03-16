from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    real_name = forms.CharField(max_length = 20, min_length= 2)
    class Meta:
        model = User
        fields = ('username', 'real_name')
  

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User