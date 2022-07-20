from django.contrib import admin
from core.models import Evento
# Register your models here.

class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_evento', 'data_criacao','id')#Acrescenta tipo um data-tables no site do admin
    list_filter = ('titulo',)#Acrescenta um filtro no site do admin

admin.site.register(Evento, EventoAdmin)