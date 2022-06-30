
from django.shortcuts import render,redirect
from .models import Trade,Note,Market
from .forms import NuevoTrade,NuevaTradingnote,NuevoMercado
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView

from django.contrib.auth.forms import AuthenticationForm #formulario de autenticacion 
from django.contrib.auth import login,logout, authenticate


def buscar_trade(request):
    if request.method == "POST":
        simbolo=request.POST["simbolo"]
        
        trades = Trade.objects.filter(simbolo__icontains=simbolo)
        return render(request,'tradingbookapp/buscar_trade.html',{"trades":trades})
    
    
    else: #GET Y otros
        trades = []
        return render(request,'tradingbookapp/buscar_trade.html',{"trades":trades})


def buscar_note(request):
    
    
    notesexistente = []
    return render(request,'tradingbookapp/buscar_note.html',{"trades":notesexistente})


def buscar_mercado(request):
    mercadosexistente = []
    return render(request,'tradingbookapp/buscar_mercado.html',{"trades":mercadosexistente})


def base(request):
    
    return render(request,'tradingbookapp/base.html',{})


def Challenge(request):
    return render (request,'tradingbookapp/challenge.html')


def crear_trade(request):
    
    if request.method =="POST":
        #post
        formulario = NuevoTrade(request.POST)
        if formulario.is_valid():
            
            info_trade = formulario.cleaned_data
            
            trade = Trade(fecha = request.POST['fecha'],simbolo = request.POST['simbolo'],posicion = request.POST['posicion'],entrada = request.POST['entrada'],target = request.POST['target'], stop = request.POST['stop'])
            trade.save()
            return redirect("Trades")
        
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


def eliminar_trade(request,trade_id):
    trade = Trade.objects.get(id=trade_id)
    trade.delete()
    return redirect("Trades")


def editar_trade(request,trade_id):
    trade = Trade.objects.get(id=trade_id)
    if request.method == "POST":
        formulario = NuevoTrade(request.POST)
        if formulario.is_valid():
            info_trade = formulario.cleaned_data
            trade.fecha = info_trade["fecha"]
            trade.simbolo = info_trade["simbolo"]
            trade.posicion = info_trade["posicion"]
            trade.entrada = info_trade["entrada"]
            trade.target = info_trade["target"]
            trade.stop = info_trade["stop"]
            trade.save()
            
            return redirect("Trades")
        
    
    
    formulario = NuevoTrade(initial={"fecha":trade.fecha,"simbolo":trade.simbolo,"posicion":trade.posicion,"entrada":trade.entrada,"target":trade.target,"stop":trade.stop,})
   
    return render(request,'tradingbookapp/formulario_trade.html',{"form":formulario})
    

def index(request):
    return render (request,'tradingbookapp/index.html')


def Login_request(request):
    
    if request.method =="POST":
        form = AuthenticationForm(request,data=request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            
            if user is not None:
                login(request,user)
                return redirect("inicio")
            else:
                return redirect('login')
        else:
            return redirect('login')
    
    form = AuthenticationForm()
        
        
    return render(request,'tradingbookapp/login.html',{"form":form})


def Markets(request):
    markets = Market.objects.all()
    ctx = {'markets':markets}
    return render(request,'tradingbookapp/markets.html',ctx)


def Notes(request):
    notes = Note.objects.all()
    ctx = {'notes':notes}
    return  render (request,'tradingbookapp/notes.html',ctx)


def Trades(request):
    if request.method=="POST":
        search = request.POST["search"] # este search viene del nombre del cuadro de busqueda de la vista
        if search !="":
            trades = Trade.objects.filter(Q(simbolo__icontains=search)|Q(simbolo__icontains=search)).values()
            return render(request,'tradingbookapp/trades.html',{"trades":trades,"search":True,"busqueda":search})
    
    #read
    trades = Trade.objects.all()
    ctx = {'trades':trades}
    return render(request,'tradingbookapp/trades.html',ctx)


class TradesList(ListView):#lista todos los estudiantes (read)
    model = Trade 
    template_name = "tradingbookapp/trade_list.html"
    
class TradesDetail(DetailView):
    model = Trade
    template_name = "tradingbookapp/trade_detail.html"
    
class TradeCreate(CreateView):
    model = Trade
    success_url = "/tradingbook/trades/list" #atencion a la primera barra!!!!!! 
    fields = ["fecha","simbolo","posicion","entrada","target","stop"]


class TradeUpdate(UpdateView):
    model = Trade
    success_url = "/tradingbook/trades/list" #atencion a la primera barra!!!!!! 
    fields = ["fecha","simbolo","posicion","entrada","target","stop"]

   
class TradeDelete(DeleteView):
     model = Trade
     success_url = "/tradingbook/trades/list" #atencion a la primera barra!!!!!! 
  
    
    
    
    


