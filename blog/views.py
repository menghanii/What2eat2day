from django.shortcuts import get_object_or_404, render, redirect
from .models import Post, Comment
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET, require_http_methods, require_POST
from .forms import PostModelForm, CommentModelForm
from .models import Post, Comment
import requests
import json
from .maps import headers, url, na_id

#---- 첫 화면 페이지 함수 ----
def main_page(request):
    menu_type = request.POST.get('menu') # 메뉴 별로 볼 수도 있게 가능하게 하기 위해 만들어 놓음.
    posts = Post.objects.all().order_by('-created_date') # 전체 포스팅을 최신 글 순으로 보여주기 위해 만듦.
    last_post = Post.objects.order_by('created_date').last() # 가장 최신글 몇몇 개를 Carousel 형식으로 보여주기 위해 만듦.
    if menu_type:
        posts = posts.filter(menu=menu_type)
    return render(request, 'blog/main_page.html', {
        'posts':posts,
        'last_post':last_post,
        })


#---- 각 포스팅 글에 들어갔을 때 함수----
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id) # 각 포스팅 글
    comments = post.comments.all() # 각 포스팅 글에 있는 댓글

    # 네이버 지도 API 에서 주소 경도, 위도 요청
    params = {'query': post.address}
    res = requests.get(url, headers=headers, params=params)
    temp = res.json()
    # 주소가 검색되는 지 여부 판단! // 검색이 안되면 네이버 본사 위도 경도가 기본 검색 값
    if temp['status'] == 'INVALID_REQUEST':
        x = 37.3591614
        y = 127.1054221
        message = '주소를 찾을 수 없습니다.'
        
    else:
        x = temp['addresses'][0]['y'] # 위도
        y = temp['addresses'][0]['x'] # 경도
        message = 0
        

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'x':x,
        'y':y,
        'id':na_id, # 네이버 지도 API _ Secret Key
        'message':message
    })

#---- 포스팅 생성 함수----
@login_required
@require_http_methods(['GET', 'POST']) 
def post_create(request):
    if request.method =='POST':
        form = PostModelForm(request.POST, request.FILES) # request.FILES는 이미지 때문에 써줌 // forms.py에서 만들어준 포스팅 형식을 이용
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog:post_detail', post.id)
    else:
        form = PostModelForm()
    return render(request, 'blog/form.html',
    {
        'form':form,
    })

#---- 포스팅 수정 함수----
@login_required 
@require_http_methods(['GET', 'POST']) 
def post_update(request, post_id):
    post = get_object_or_404(Post, id=post_id) # 해당 글 불러오기 or 404 에러

    if post.author != request.user: # 글 수정 요청자와 글쓴이가 같아야 실행 
        return redirect('blog:main_page')

    if request.method =='POST':
        form = PostModelForm(request.POST, request.FILES, instance=post) # 수정이니 기존에 내용이 있어야 함. // 고로 instance 사용
        if form.is_valid():
            post = form.save()
            return redirect('blog:post_detail', post.id)
    else:
        form = PostModelForm(instance=post)
    return render(request, 'blog/form.html',
    {
        'form':form,
    })

#---- 포스팅 삭제 함수----
@login_required
@require_http_methods(['GET', 'POST']) 
def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.author == request.user: # 삭제 요청와 글쓴이가 같아야만 실행
        post.delete()
    return redirect('blog:main_page')


#---- 댓글 생성 함수----
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


#---- 댓글 삭제 함수----
@login_required
@require_POST
def delete_comment(request, post_id, comment_id): # 포스팅 id와 댓글 id가 필요
    comment = get_object_or_404(Comment, post_id=post_id, id=comment_id)
    # post = get_object_or_404(Post, id=post_id)
    if request.user == comment.author: # 삭제 요청자와 댓글 글쓴이가 같아야만 실행
        # if article.comments_num != 0:
        #     article.comments_num -=1
        # else:
        #     article.comments_num = 0
        comment.delete()
        # article.save()
    return redirect('blog:post_detail', comment.post.id)


#---- '신촌 안' 페이지 (a 태그 때문에 request요청에서 value 값을 받아올 수 없었음 // 고로 페이지 관련 함수를 2개 만듦...)----
def bulletin_1(request):
    posts = Post.objects.filter(bulletin='1').order_by('-created_date')
    name = '신촌'
    menu_type = request.POST.get('menu') # 메뉴 별 보기 때문에
    if menu_type:
        posts = posts.filter(menu=menu_type)
    return render(request, 'blog/bulletin.html', {
        'name':name,
        'posts':posts,
        })


#---- '신촌 밖' 페이지----
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


#---- 좋아요 기능 구현----
@login_required
def like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user
    # if post.like_users.filter(id=user.id).exists():
    if user in post.like_users.all(): # 이미 좋아요 상태면
        post.like_users.remove(user) # 지움
    else:
        post.like_users.add(user) # 아닐 경우 추가
    return redirect('blog:post_detail', post.id)