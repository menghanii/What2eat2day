from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
# from ckeditor_uploader.widgets import CKEditorUploadingWidget

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    # real_name = forms.CharField(max_length = 20, min_length= 2)
    class Meta:
        model = User
        fields = ('username', 'real_name')
        # widgets = {
        #     'username': forms.TextInput(
        #         attrs={'size': 12, 'class': 'form-control', 'style': 'width: 30%', 'placeholder': '아이디를 적어주세요~'}
        #     ),
        #     'real_name': forms.TextInput(
        #         attrs={'size': 12, 'class': 'form-control', 'style': 'width: 30%', 'placeholder': '이름을 적어주세요~'},
        #     ),
        # }
  

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User