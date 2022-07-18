from django.shortcuts import render, HttpResponse, redirect
from core.models import Evento
# Create your views here.

def lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario = usuario)
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)

#def index(request):
    #return redirect('/agenda/')
   