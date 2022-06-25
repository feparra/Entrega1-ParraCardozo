from django.urls import path

from . import views #se utiliza el punto por que es la ruta relativa (donde esta la carpeta)

urlpatterns = [
    path('',views.index, name='index'),
    path('dashboard/',views.Dashboard,name="dashboard"),
    path('notes/',views.Notes,name="notes"),
    path('trades/',views.Trades,name="trades"),
    
]
