from django.shortcuts import render, HttpResponse, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.
def login_user(request):
    return render(request,'login.html')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request,usuario)
            return redirect('/')
        else:
            messages.error(request,"Usuário ou senha inválidos")
    
    return redirect('/')

@login_required(login_url='/login/')

def lista_eventos(request):
    user = request.user
    evento = Evento.objects.filter(usuario = user)
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)

def logout_user(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/login/')

def evento(request):
    id_evento = request.GET.get('id')
    dados = {}
    if id_evento:
        dados['evento'] = Evento.objects.get(id=id_evento)
    return render(request,'evento.html', dados)

@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        desc = request.POST.get('descricao')
        local = request.POST.get('local')
        usuario = request.user
        id_evento = request.POST.get('id')
        if id_evento:
            evento = Evento.objects.get(id=id_evento)

            if evento.usuario == usuario:
                evento.titulo = titulo
                evento.descricao = desc
                evento.local = local
                evento.data_evento = data_evento
                evento.save()
            #Evento.objects.filter(id=id_evento).update(
                #titulo=titulo,
                #data_evento=data_evento,
                #descricao=desc,
                #local=local,
            #)
        else:
            usuario = request.user
            Evento.objects.create(titulo=titulo,
                                data_evento=data_evento,
                                descricao=desc,
                                local=local,
                                usuario=usuario,
                                )
    return redirect('/')

@login_required(login_url='/login/')

def delete_evento(request,id_evento):
    user = request.user
    evento = Evento.objects.get(id = id_evento)
    if user == evento.usuario:
        evento.delete()
    return redirect('/')
    

#def index(request):
    #return redirect('/agenda/')

