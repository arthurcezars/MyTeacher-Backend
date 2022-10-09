from django.contrib import admin
from .models import *

class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'valor_hora', 'descricao')
    list_display_links = ('nome', 'valor_hora', 'descricao')
    empty_value_display = 'Vazio'
    search_fields = ('nome',)

# Register your models here.
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Aula)