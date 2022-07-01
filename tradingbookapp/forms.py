from django import forms
from django.forms.widgets import NumberInput
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm #formulario de autenticacion 
from django.contrib.auth.models import User
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
    
    
class UserRegisterform(UserCreationForm):
    
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Password",widget=forms.PasswordInput) # lacontrasena no se ve 
    password2: forms.CharField(label="Password",widget=forms.PasswordInput)
    
    class Meta:
        model = User 
        fields=['username','email','password1','password2']
        help_texts = {k:"" for k in fields}
    
    