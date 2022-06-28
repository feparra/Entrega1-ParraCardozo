from django.contrib import admin

from .models import Trade,Note,Market

class TradeAdmin(admin.ModelAdmin):
    list_display=("fecha","simbolo" , "posicion" , "entrada" , "target" ,"stop")
    search_fields =("fecha","simbolo" , "posicion" , "entrada" , "target" ,"stop")
    
class NoteAdmin(admin.ModelAdmin):
    list_display=("fecha","simbolo" )
    search_fields =("fecha","simbolo")
    
class MarketAdmin(admin.ModelAdmin):
    list_display=("mercado","simbolo" )
    search_fields =("mercado","simbolo")

admin.site.register(Trade,TradeAdmin)
admin.site.register(Note,NoteAdmin)
admin.site.register(Market,MarketAdmin)

