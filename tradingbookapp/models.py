from django.db import models

class Trade(models.Model):
    fecha = models.DateField("Fecha de operacion",unique=True, null=True)
    simbolo = models.CharField("Simbolo",max_length=30)
    
    posiciones = (
        (1,"Long"),
        (2,"Short")
    )
    posicion = models.PositiveSmallIntegerField("Posicion",choices=posiciones)
    entrada = models.FloatField("Precio Entrada",)
    target = models.FloatField("Target")
    stop = models.FloatField("stop")
    
class Notes(models.Model):
    fecha = models.DateField("Fecha de operacion",unique=True, null=True) 
    nota = models.CharField("Notas de trading", max_length=250)
    
    
class Mercados(models.Model):
    mercado = models.CharField("Watch List", max_length=250)