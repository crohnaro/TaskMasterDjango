from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('task/', views.task_view, name='task'),
]
