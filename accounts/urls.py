from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('<int:user_id>/', views.accounts_detail, name='accounts_detail'),
    # path('follow/<int:user_id>/', views.follow, name='follow'),
]