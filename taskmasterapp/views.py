from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == "POST":
        # Lógica de login
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('task')  # Redireciona para a página de tarefas após login bem-sucedido
        else:
            return render(request, 'login/index.html', {'error': 'Credenciais inválidas'})
    
    # Se o método for GET, exibe o formulário de login
    return render(request, 'login/index.html')

def task_view(request):
    return render(request, 'task/index.html')
