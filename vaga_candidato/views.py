from django.shortcuts import render, get_object_or_404
from .models import Vaga, Candidato
from .forms import VagaForm, CandidatoForm


def lista_candidatos(request):
    candidatos = Candidato.objects.select_related('vaga')
    return render(request, 'vaga_candidato/index.html', {'candidatos': candidatos})


def candidato_detalhe(request, candidato_id):
    candidato = get_object_or_404(Candidato, id=candidato_id)
    return render(request, 'vaga_candidato/candidato_detalhe.html', {'candidato': candidato})


def vaga_detalhe(request, vaga_id):
    vaga = get_object_or_404(Vaga, id=vaga_id)
    return render(request, 'vaga_candidato/vaga_detalhe.html', {'vaga': vaga})


def candidato_formulario(request):
    form = CandidatoForm()
    return render(request, 'vaga_candidato/candidato_form.html', {'form': form})


def vaga_formulario(request):
    form = VagaForm()
    return render(request, 'vaga_candidato/vaga_form.html', {'form': form})
