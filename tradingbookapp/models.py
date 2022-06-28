from django.db import models
import datetime

class Trade(models.Model):
    fecha = models.DateField("Fecha de operacion (mm/dd/yyyy)",auto_now_add=False,auto_now=False,blank=True,null=True)
    simbolo = models.CharField("Simbolo",max_length=30)
    
    posiciones = (
        (1,"Long"),
        (2,"Short")
    )
    posicion = models.PositiveSmallIntegerField("Posicion",choices=posiciones)
    entrada = models.FloatField("Precio Entrada",)
    target = models.FloatField("Target")
    stop = models.FloatField("stop")
    
class Note(models.Model):
    fecha = models.DateField("Fecha de operacion (mm/dd/yyyy)",auto_now_add=False,auto_now=False,blank=True,null=True)
    simbolo = models.CharField("Simbolo",max_length=30)
    nota = models.CharField("Notas de trading", max_length=250)
    
    
class  Market(models.Model):
    pais = models.CharField("pais a donde pertenece",max_length=30)
    simbolo = models.CharField("Simbolo a observar",max_length=30)