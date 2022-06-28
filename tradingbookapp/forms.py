from django import forms

class NuevoTrade(forms.Form):
    simbolo = forms.CharField()
    entrada = forms.IntegerField()
    