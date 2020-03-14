from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('<int:post_id>/', views.post_detail, name='post_detail'),
]

