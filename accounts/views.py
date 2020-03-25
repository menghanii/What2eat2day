from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth import get_user_model
from blog.models import Post, Comment
from .models import User

#---- 회원가입 함수----
@require_http_methods(['GET', 'POST'])
def signup(request):

    # 이미 가입이 되었을 경우
    if request.user.is_authenticated:
        return redirect('blog:main_page')

    # 새 가입
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('blog:main_page')
    else:
        form = CustomUserCreationForm()

    return render(request, 'accounts/form.html',
    {
        'form': form,
    })


#---- 로그인 함수----
def login(request):
    
    # 이미 로그인 되어 있을 경우, 메인페이지로 보내기
    if request.user.is_authenticated:
        return redirect('blog:main_page')
    
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('blog:main_page')

    else:
        form = CustomAuthenticationForm()

    return render(request, 'accounts/form.html',
    {
        'form': form,
    })


#---- 로그아웃 함수----
@login_required
def logout(request):
    auth_logout(request)
    return redirect('blog:main_page')


#---- Mypage 함수----
@login_required
@require_GET
def accounts_detail(request, user_id):
    account = get_object_or_404(User, id=user_id)
    posts = Post.objects.filter(author=account).order_by('-created_date') # 본인이 올린 게시글 찾기
    likes = Post.objects.filter(like_users=account).order_by('-created_date') # 본인이 좋아하는 글 찾기
    return render(request, 'accounts/accounts_detail.html', {
        'account':account,
        'posts':posts,
        'likes': likes,

    })


# @require_POST
# def follow(request, user_id):
#     fan = request.user
#     star = get_object_or_404(User, id=user_id)

#     if fan != star:
#         if star.fans.filter(id=fan.id).exists():
#             star.fans.remove(fan)
#         else:
#             star.fans.add(fan)

#     return redirect('accounts:accounts_detail', star.id)