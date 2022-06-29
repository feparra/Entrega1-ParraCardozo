from django.urls import path

from . import views #se utiliza el punto por que es la ruta relativa (donde esta la carpeta)

urlpatterns = [
    path('',views.index, name='Home'),
    path('dashboard/',views.Dashboard,name="Dashboard"),
    path('eliminar_trade/<trade_id>',views.eliminar_trade,name="Eliminar_trade"),
    path('editar_trade/<trade_id>',views.editar_trade,name="Editar_trade"),
    
    path('notes/',views.Notes,name="Notes"),
    path('trades/',views.Trades,name="Trades"),
    path('markets/',views.Markets,name="Markets"),
    path('challenge/',views.Challenge,name="Challenge"),
    path('crear_trades/',views.crear_trade,name="crear_trades"),
    path('buscar_trades/',views.buscar_trade,name="buscar_trades"),
    path('buscar_notes/',views.buscar_note,name="buscar_notes"),
    path('buscar_mercados/',views.buscar_mercado,name="buscar_trades"),
    path('crear_notes/',views.crear_notes,name="crear_notes"),
    path('crear_mercados/',views.crear_mercados,name="crear_mercados"),
    # path('base/', views.base),
    
]
