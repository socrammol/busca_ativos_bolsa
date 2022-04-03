from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username','ticker','tempomonitoramento','iniciomonitoramentoemdias','terminomonitoramentoemdias','email','valormenor','valormaior']