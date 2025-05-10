from django.contrib import admin
from .models import Vaga, Candidato


@admin.register(Vaga)
class VagaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'area', 'tipo_contrato')
    list_filter = ('area', 'tipo_contrato')
    search_fields = ('area', 'tipo_contrato')


@admin.register(Candidato)
class CandidatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'vaga__titulo')
    list_filter = ('vaga__titulo', 'vaga__area', 'vaga__tipo_contrato')
    search_fields = ('nome', 'email')
