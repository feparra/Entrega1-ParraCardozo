from django.shortcuts import render
from .models import Trade


def index(request):
    return render (request,'tradingbookapp/index.html')


def Trades(request):
    trades = Trade.objects.all()
    ctx = {'trades':trades}
    return render(request,'tradingbookapp/Trades.html',ctx)

def Dashboard(request):
    
    trades = Trade.objects.all()
    ctx = {'trades':trades}
    return  render (request,'tradingbookapp/dashboard.html',ctx)

def Notes(request):
    pass
    return  render (request,'tradingbookapp/notes.html')

