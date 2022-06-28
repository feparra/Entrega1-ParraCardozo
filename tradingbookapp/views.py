from django.shortcuts import render,redirect
from .models import Trade,Note,Market


def index(request):
    return render (request,'tradingbookapp/index.html')


def Challenge(request):
    return render (request,'tradingbookapp/challenge.html')


def Trades(request):
    trades = Trade.objects.all()
    ctx = {'trades':trades}
    return render(request,'tradingbookapp/Trades.html',ctx)

def Markets(request):
    markets = Market.objects.all()
    ctx = {'mercados':markets}
    return render(request,'tradingbookapp/watchlist.html',ctx)

def base(request):
    
    return render(request,'tradingbookapp/base.html',{})



def crear_trade(request): 
    #post
    if request.method =="POST":
        trade = Trade(fecha = request.POST['fecha'],simbolo = request.POST['simbolo'],posicion = request.POST['posicion'],entrada = request.POST['entrada'],target = request.POST['target'], stop = request.POST['stop'])
        trade.save()
        return redirect("Home")
        
    else:
        return render(request,'tradingbookapp/formulario_trade.html')


def crear_notes(request):
    
    if request.method =="POST":
        note = Note(fecha = request.POST['fecha'],simbolo = request.POST['simbolo'],nota = request.POST['nota'])
        note.save()
        return redirect("Home")
        
    else:
        return render(request,'tradingbookapp/formulario_notes.html')

def crear_mercados(request):
    if request.method =="POST":
        mercado = Mercado(mercado= request.POST['mercado'])
        mercado.save()
        return redirect("Home")
        
    else:    
        return render(request,'tradingbookapp/formulario_mercados.html')


def Dashboard(request):
    
    trades = Trade.objects.all()
    ctx = {'trades':trades}
    return  render (request,'tradingbookapp/dashboard.html',ctx)

def Notes(request):
    notes = Note.objects.all()
    ctx = {'notes':notes}
    return  render (request,'tradingbookapp/notes.html',ctx)

