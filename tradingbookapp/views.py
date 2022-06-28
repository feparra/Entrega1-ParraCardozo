from django.shortcuts import render
from .models import Trade


def index(request):
    return render (request,'tradingbookapp/index.html')


def Trades(request):
    trades = Trade.objects.all()
    ctx = {'trades':trades}
    return render(request,'tradingbookapp/Trades.html',ctx)

def base(request):
    
    return render(request,'tradingbookapp/base.html',{})



def crear_trade(request):
    return render(request,'tradingbookapp/formulario_trade.html')


def crear_notes(request):
    return render(request,'tradingbookapp/formulario_notes.html')

def crear_mercados(request):
    return render(request,'tradingbookapp/formulario_mercados.html')


def Dashboard(request):
    
    trades = Trade.objects.all()
    ctx = {'trades':trades}
    return  render (request,'tradingbookapp/dashboard.html',ctx)

def Notes(request):
    pass
    return  render (request,'tradingbookapp/notes.html')

