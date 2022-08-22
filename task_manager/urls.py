"""task_manager URL Configuration

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
from task_manager import views
from django_filters.views import FilterView
from .models import *

urlpatterns = [
    path('', views.base, name='home'),
    # path('users/', views.users, name='users'),
    path('users/', views.UserList.as_view(), name='users_list'),
    path('users/<int:pk>/details/', views.UsersDetail.as_view(), name='users_details'),
    path('users/create/', views.UserCreate.as_view(), name='users_create'),
    path('users/<int:pk>/update/', views.UserUpdate.as_view(), name='users_update'),
    path('users/<int:pk>/delete/', views.UserDelete.as_view(), name='users_delete'),
    path('login/', views.LoginUser.as_view(), name='user_login'),
    path('logout/', views.logout_user, name='user_logout'),
    path('admin/', admin.site.urls),
    path('test/', views.TestPage.as_view(), name="test_page"),
    path('test2/', views.TestPage2.as_view(), name="test_page2"),
    path('statuses/', views.StatusList.as_view(), name='statuses_list'),
    path('statuses/create/', views.StatusCreate.as_view(), name='statuses_create'),
    path('statuses/<int:pk>/update/', views.StatusUpdate.as_view(), name='statuses_update'),
    path('statuses/<int:pk>/delete/', views.StatusDelete.as_view(), name='statuses_delete'),
    path('tasks/', views.TaskList.as_view(), name='tasks_list'),
    path('tasks/create/', views.TaskCreate.as_view(), name='tasks_create'),
    path('tasks/<int:pk>/update/', views.TaskUpdate.as_view(), name='tasks_update'),
    path('tasks/<int:pk>/delete/', views.TaskDelete.as_view(), name='tasks_delete'),
    path('tasks/<int:pk>/', views.TaskDetail.as_view(), name='tasks_detail'),
    path('labels/', views.LabelList.as_view(), name='labels_list'),
    path('labels/create/', views.LabelCreate.as_view(), name='labels_create'),
    path('labels/<int:pk>/update/', views.LabelUpdate.as_view(), name='labels_update'),
    path('labels/<int:pk>/delete/', views.LabelDelete.as_view(), name='labels_delete'),
    path('tasks3/', views.TaskList2.as_view(), name='tasks3_list'),
    # path('tasks2/', views.task_list_2, name="tasks2_list"),
]
