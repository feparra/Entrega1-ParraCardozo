from django.urls import path

from . import views #se utiliza el punto por que es la ruta relativa (donde esta la carpeta)

urlpatterns = [
    path('',views.index, name='Home'),
    path('dashboard/',views.Dashboard,name="Dashboard"),
    path('notes/',views.Notes,name="Notes"),
    path('trades/',views.Trades,name="Trades"),
        path('crear_trades/',views.crear_trade,name="crear_trades"),
    # path('base/', views.base),
    
]
