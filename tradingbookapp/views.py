from django.shortcuts import render
from .models import Trade


def index(request):
    trades = Trade.objects.all()
    ctx = {'trades':trades}
    return render (request,'tradingbookapp/index.html',ctx)
