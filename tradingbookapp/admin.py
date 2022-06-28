from django.contrib import admin

from .models import Trade

class TradeAdmin(admin.ModelAdmin):
    list_display=("simbolo" , "posicion" , "entrada" , "target" ,"stop")
    search_fields =("simbolo" , "posicion" , "entrada" , "target" ,"stop")

admin.site.register(Trade,TradeAdmin)

