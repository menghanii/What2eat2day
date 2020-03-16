from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from .models import Post, Comment
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET, require_http_methods, require_POST
from .forms import PostModelForm, CommentModelForm
from .models import Post, Comment
# from django.http import JsonResponse, HttpResponseBadRequest

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
        comment.article = post
        comment.author = request.user
        comment.save()
        # article.comments_num +=1
        # article.save()
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


# @login_required
# # @require_POST
# def toggle_like(request, post_id):
#     if request.is_ajax:
#         post = get_object_or_404(Post, id=post_id)
#         user = request.user

#         # 좋아요를 누른 user 라면,
#         if post.like_users.filter(id=user.id).exists():
#             post.like_users.remove(user)
#             liked = False
#         else:
#             post.like_users.add(user)
#             liked = True
    
#         context = {'liked': liked, 'post_id': post.id, 'user_id': user.id}
#         return JsonResponse(context)
#     else:
#         return HttpResponseBadRequest()