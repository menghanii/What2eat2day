from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from .models import Post, Comment
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET, require_http_methods, require_POST
from .forms import PostModelForm, CommentModelForm
from .models import Post, Comment
import requests
import json
# from django.http import JsonResponse, HttpResponseBadRequest

def main_page(request):
    menu_type = request.POST.get('menu')
    posts = Post.objects.all().order_by('-created_date')
    last_post = Post.objects.order_by('created_date').last()
    if menu_type:
        posts = posts.filter(menu=menu_type)
    return render(request, 'blog/main_page.html', {
        'posts':posts,
        'last_post':last_post,
        })
        
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()
    url = "https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode"
    headers = {'Accept': 'application/json', 'X-NCP-APIGW-API-KEY-ID': 'r1e5o8jg6h', 'X-NCP-APIGW-API-KEY': 'jHsTAMcR2u67EhiqscUtZIkv2qSNnvWATmW1FRUp'}
    params = {'query': post.address}
    res = requests.get(url, headers=headers, params=params)
    temp = res.json()
    x = temp['addresses'][0]['y']
    y = temp['addresses'][0]['x']
    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'x':x,
        'y':y,
    })

@login_required
@require_http_methods(['GET', 'POST']) 
def post_create(request):
    if request.method =='POST':
        form = PostModelForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # post.author_id = request.user_id
            post.save()
            return redirect('blog:post_detail', post.id)
    else:
        form = PostModelForm()
    return render(request, 'blog/form.html',
    {
        'form':form,
    })


@login_required 
@require_http_methods(['GET', 'POST']) 
def post_update(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if post.author != request.user:
        return redirect('blog:main_page')

    if request.method =='POST':
        form = PostModelForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('blog:post_detail', post.id)
    else:
        form = PostModelForm(instance=post)
    return render(request, 'blog/form.html',
    {
        'form':form,
    })

@login_required
@require_http_methods(['GET', 'POST']) 
def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.author == request.user:
        post.delete()
    return redirect('blog:main_page')


@login_required
@require_POST
def create_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    form = CommentModelForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False) # 아직 posting_id가 비어있기 때문에, 저장하는 척만 하고 Comment 객체 return
        # comment.article_id = article.id
        comment.post = post
        comment.author = request.user
        comment.save()
        # article.comments_num +=1
        post.save()
    return redirect('blog:post_detail', post.id)

@login_required
@require_POST
def delete_comment(request, post_id, comment_id):
    comment = get_object_or_404(Comment, post_id=post_id, id=comment_id)
    # post = get_object_or_404(Post, id=post_id)
    if request.user == comment.author:
        # if article.comments_num != 0:
        #     article.comments_num -=1
        # else:
        #     article.comments_num = 0
        comment.delete()
        # article.save()
    return redirect('blog:post_detail', comment.post.id)


def bulletin_1(request):
    posts = Post.objects.filter(bulletin='1').order_by('-created_date')
    name = '신촌'
    menu_type = request.POST.get('menu')
    if menu_type:
        posts = posts.filter(menu=menu_type)
    return render(request, 'blog/bulletin.html', {
        'name':name,
        'posts':posts,
        })

def bulletin_2(request):
    posts = Post.objects.filter(bulletin='2').order_by('-created_date')
    name = '신촌 밖'
    menu_type = request.POST.get('menu')
    if menu_type:
        posts = posts.filter(menu=menu_type)
    return render(request, 'blog/bulletin.html', {
        'name':name,
        'posts':posts,
        })

@login_required
def like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user
    # if article.like_users.filter(id=user.id).exists():
    if user in post.like_users.all(): # 이미좋아요 상태
        post.like_users.remove(user) # 고로 지움
    else:
        post.like_users.add(user)
    return redirect('blog:post_detail', post.id)