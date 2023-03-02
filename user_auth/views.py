from asyncio import constants
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib import auth


def register(request):
  if request.method == 'GET':
    if request.user.is_authenticated:
      return redirect('/')
    return render(request, 'register.html')
  elif request.method == 'POST':
    username = request.POST.get('username')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    if len(username.strip()) == 0 or len(email.strip()) == 0 or len(senha.strip()) == 0: 
      messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
      return redirect('/auth/register')
    
    user = User.objects.filter(username = username)
    
    if user.exists():
      messages.add_message(request, constants.ERROR, 'Já existe um usuário com esse nome cadastrado')
      return redirect('/auth/register')
    
    try:
      user = User.objects.create_user(
        username = username,
        email = email,
        password = senha
      )
      messages.add_message(request, constants.SUCCESS, 'Cadastro realizado com sucesso')
      user.save()
      return redirect('/auth/login')
    except:
      messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
      return redirect('auth/login')
    

def login(request):
  if request.method == 'GET':
    if request.user.is_authenticated:
      return redirect('/')
    return render(request, 'login.html')
  elif request.method =='POST':
    username = request.POST.get('username')
    senha = request.POST.get('senha')
    
    user = auth.authenticate(username=username, password=senha)
    if not user:
      messages.add_message(request, constants.ERROR, 'Usuario ou senha invalido!!')
      return redirect('login')
    else:
     auth.login(request, user)
     return redirect('/')
   
      