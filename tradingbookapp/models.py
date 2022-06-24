from django.db import models

class Trade(models.Model):
    simbolo = models.CharField("Simbolo",max_length=30)
    posiciones = (
        (1,"Long"),
        (2,"Short")
    )
    posicion = models.PositiveSmallIntegerField("Posicion",choices=posiciones)
    entrada = models.FloatField("Precio Entrada",)
    target = models.FloatField("Target")
    stop = models.FloatField("stop")
    
