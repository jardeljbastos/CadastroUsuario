from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    return render(request, 'home.html')

# Formulario de cadastro de usuarios
def create(request):
    return render(request, 'create.html')

# Inserção dos dados dos usuários no banco
def store(request):
    data = {}
    if(request.POST['password'] != request.POST['password_conf']):
        data['msg'] = 'Senha e confirmação de senha diferentes!'
        data['class'] = 'alert-danger'
    else:
        user = User.objects.create_user(request.POST['user'], request.POST['email'], request.POST['password'])
        user.first_name = request.POST['name']
        user.save()
        user.user_permissions.add(25)
        data['msg'] = 'Usuario cadastrado com sucesso!'
        data['class'] = 'alert-success'
    return render(request, 'create.html',data)

#Formulário de Painel de Login
def painel(request):
    return render(request, 'painel.html')


#Processa o login
def dologin(request):
    data={}
    user = authenticate(username=request.POST['user'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect('/dashboard/')
    else:
        data['msg'] = 'Usuário ou Senha inválidos!'
        data['class'] = 'alert-danger'
    return render(request, 'painel.html',data)

#Página inicial do dashboard
def dashboard(request):
    return render(request, 'dashboard/home.html')

#Logout do sistema
def logouts(request):
    logout(request)
    return redirect('/painel/')

#Alterar a senha
def changePassword2(request):
    #return render(request, 'changePassword.html/')
    user = User.objects.get(email=request.user.email)
    user.set_password(request.POST['passwordnew'])
    user.save()
    logout(request)
    return redirect('/painel/')

def changePassword(request):
    return render(request, 'changePassword.html/')