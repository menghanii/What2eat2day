from django import forms
from .models import Post, Comment

class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'bulletin', 'menu', 'image', 'image_2', 'image_3', 'image_4', 'text',)


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)