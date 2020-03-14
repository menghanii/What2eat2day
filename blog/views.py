from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from .models import Post, Comment

def main_page(request):
    posts = Post.objects.all().order_by('-created_date')
    last_post = Post.objects.order_by('created_date').last()
    return render(request, 'blog/main_page.html', {
        'posts':posts,
        'last_post':last_post,
        })


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()
    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
    })