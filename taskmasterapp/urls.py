from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('task/', views.task_view, name='task'),
    path('register/', views.register_view, name='register'),
    path('taskregister/', views.task_register, name='taskregister'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),  # Rota para editar
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),  # Rota para deletar
]
