from django import forms
from django.forms.widgets import NumberInput

posiciones=(
    ("1","Long"),
    ("2","Short"),
    
)
class NuevoTrade(forms.Form):
    fecha = forms.DateTimeField(label="fecha ", required=True, widget=NumberInput(attrs={'type':'date'}))
    simbolo = forms.CharField(label="simbolo")
    posicion = forms.ChoiceField(label="posicion",choices=posiciones)
    entrada = forms.FloatField(label="Precio Entrada",)
    target = forms.FloatField(label="Target")
    stop = forms.FloatField(label="stop")

class NuevaTradingnote(forms.Form):
    fecha = forms.DateTimeField(label="fecha ", required=True, widget=NumberInput(attrs={'type':'date'}))
    simbolo = forms.CharField(label="simbolo")
    nota = forms.CharField(label="Nota",widget=forms.Textarea(attrs={"rows":5, "cols":30}))


class NuevoMercado(forms.Form):
    pais =forms.CharField(label="pais")
    simbolo = forms.CharField(label="simbolo")
    
    
