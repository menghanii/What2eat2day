from django import forms
from .models import Post, Comment
# from ckeditor_uploader.widgets import CKEditorUploadingWidget
 

class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'bulletin', 'menu', 'address', 'image', 'image_2', 'image_3', 'image_4', 'text',)

        # widgets = {
        #     'title': forms.TextInput(
        #         attrs={'size': 12, 'class': 'form-control', 'style': 'width: 70%', 'placeholder': '어디에 다녀오셨나요~?'}
        #     ),
        #     'bulletin': forms.Select(
        #         attrs={'class': 'custom-select', 'style': 'width: 50%',},
        #     ),
        #     'menu': forms.Select(
        #         attrs={'class': 'custom-select', 'style': 'width: 50%',},
        #     ),
        #     'text':  forms.Textarea(
        #         attrs={'size': 10,'class': 'form-control', 'style': 'width: 70%', 'placeholder': '후기를 작성해주세요! 정성껏 쓸 수록 진심이 더해집니다~'}
        #     ),
        # }


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        # widgets = {
        #     'content': forms.TextInput(
        #         attrs={'size': 12, 'class': 'form-control', 'style': 'width: 70%', 'placeholder': '한 줄 평을 남겨주세요~'}
        #     ),
        # }