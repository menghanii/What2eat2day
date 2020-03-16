from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('<int:post_id>/', views.post_detail, name='post_detail'),
    path('create/', views.post_create, name='post_create'),
    path('<int:post_id>/update/', views.post_update, name='post_update'),
    path('<int:post_id>/delete/', views.post_delete, name='post_delete'),
    path('<int:post_id>/comments/create/', views.create_comment, name='create_comment'),
    path('<int:post_id>/comment/<int:comment_id>/delete', views.delete_comment, name='delete_comment'),
]
