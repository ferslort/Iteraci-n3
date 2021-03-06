"""iteracion3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app import views
from user import views as user_views
from post import views as post_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.page_index, name="index"),
    path('logout/', user_views.logout_user, name='logout'),
    path('login/', user_views.page_login, name='login'),
    path('register/', user_views.register_page, name='register'),
    path('users/', user_views.usersList_page, name='users'),
    path('post/', post_views.post, name='post'),
    path('post/create/', post_views.create_post, name='create_post'),
    path('post/delete/<id>', post_views.delete_post, name='delete_post'),
    path('post/edit/<id>', post_views.edit_post, name='edit_post'),
]
