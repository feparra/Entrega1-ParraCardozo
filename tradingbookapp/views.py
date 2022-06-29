
from django.shortcuts import render,redirect
from .models import Trade,Note,Market
from .forms import NuevoTrade,NuevaTradingnote,NuevoMercado

def index(request):
    return render (request,'tradingbookapp/index.html')


def Challenge(request):
    return render (request,'tradingbookapp/challenge.html')


def buscar_trade(request):
    tradesexistente = []
    return render(request,'tradingbookapp/buscar_trade.html',{"trades":tradesexistente})

def buscar_note(request):
    notesexistente = []
    return render(request,'tradingbookapp/buscar_note.html',{"trades":notesexistente})

def buscar_mercado(request):
    mercadosexistente = []
    return render(request,'tradingbookapp/buscar_mercado.html',{"trades":mercadosexistente})




def Trades(request):
    trades = Trade.objects.all()
    ctx = {'trades':trades}
    return render(request,'tradingbookapp/trades.html',ctx)

def Markets(request):
    markets = Market.objects.all()
    ctx = {'markets':markets}
    return render(request,'tradingbookapp/markets.html',ctx)

def base(request):
    
    return render(request,'tradingbookapp/base.html',{})



def crear_trade(request):
    
    if request.method =="POST":
        #post
        formulario = NuevoTrade(request.POST)
        if formulario.is_valid():
            
            info_trade = formulario.cleaned_data
            
            trade = Trade(fecha = request.POST['fecha'],simbolo = request.POST['simbolo'],posicion = request.POST['posicion'],entrada = request.POST['entrada'],target = request.POST['target'], stop = request.POST['stop'])
            trade.save()
            return redirect("Home")
        
        else:
            return render(request,'tradingbookapp/formulario_trade.html',{"form":formulario})
        
    else: #get y otros:
        
        tradevacio = NuevoTrade()
        
        
        return render(request,'tradingbookapp/formulario_trade.html',{"form":tradevacio})


def crear_notes(request):
    
    if request.method =="POST":
        #post
        formulario = NuevaTradingnote(request.POST)
        if formulario.is_valid():
            
            info_note = formulario.cleaned_data
            note = Note(fecha = request.POST['fecha'],simbolo = request.POST['simbolo'],nota = request.POST['nota'])
            note.save()
            return redirect("Home")
        else:
            return render(request,'tradingbookapp/formulario_notes.html',{"form":formulario})
        
    else:
        notavacia = NuevaTradingnote()
        return render(request,'tradingbookapp/formulario_notes.html',{"form":notavacia})

def crear_mercados(request):
    if request.method =="POST":
        #post
        formulario = NuevoMercado(request.POST)
        if formulario.is_valid():

            mercado = Market(pais= request.POST['pais'],simbolo= request.POST['simbolo'])
            mercado.save()
            return redirect("Home")
        else:
            return render(request,'tradingbookapp/formulario_mercados.html',{"form":formulario})
            
    else:  
        mercadovacio = NuevoMercado()  
        return render(request,'tradingbookapp/formulario_mercados.html',{"form":mercadovacio})


def Dashboard(request):
    
    trades = Trade.objects.all()
    ctx = {'trades':trades}
    return  render (request,'tradingbookapp/dashboard.html',ctx)

def Notes(request):
    notes = Note.objects.all()
    ctx = {'notes':notes}
    return  render (request,'tradingbookapp/notes.html',ctx)

