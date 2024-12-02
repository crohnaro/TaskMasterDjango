from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('task/', views.task_view, name='task'),
    path('register/', views.register_view, name='register'),
    path('taskregister/', views.task_register, name='taskregister'),
]
