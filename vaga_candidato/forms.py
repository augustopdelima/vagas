from django import forms
from .models import Vaga, Candidato


class VagaForm(forms.ModelForm):
    class Meta:
        model = Vaga
        fields = "__all__"


class CandidatoForm(forms.ModelForm):
    class Meta:
        model = Candidato
        fields = "__all__"
