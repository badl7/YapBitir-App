from django.forms import CheckboxInput
from django.shortcuts import get_object_or_404, redirect, render,HttpResponse,redirect,get_object_or_404,reverse

import yapbitir
from .forms import YapbitirForm
from django.contrib import messages
from .models import Yapbitir
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    ara = request.GET.get("ara")

    if ara:
        yapbitirs = Yapbitir.objects.filter(title__contains = ara)
        return render(request,"yapbitirs.html", {"yapbitirs" : yapbitirs})
    yapbitirs = Yapbitir.objects.all()
    return render(request, "index.html", {"yapbitirs" : yapbitirs})
#    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def yapbitirs(request):
    keyword = request.GET.get("keyword")

    if keyword:
        yapbitirs = Yapbitir.objects.filter(title__contains = keyword)
        return render(request,"yapbitirs.html", {"yapbitirs" : yapbitirs})
    yapbitirs = Yapbitir.objects.all()
    return render(request, "yapbitirs.html", {"yapbitirs" : yapbitirs})


@login_required(login_url="user:login")
def dashboard(request):
    yapbitirs = Yapbitir.objects.filter(author = request.user)
    return render(request , "dashboard.html",{"yapbitirs" : yapbitirs})


@login_required(login_url="user:login")
def addyapbitir(request):
    form = YapbitirForm(request.POST or None, request.FILES or None)
    content = CheckboxInput
    
    if form.is_valid():
        
        yapbitir = form.save(commit=False)
        
        yapbitir.author = request.user
        yapbitir.save()

        messages.success(request,"Liste Başarıyla Eklenmiştir...")
        return redirect("yapbitir:dashboard")

    return render(request, "addyapbitir.html", {"form" : form})


def detail(request,id):
    #article = Yapbitir.objects.filter(id = id).first()
    yapbitir = get_object_or_404(Yapbitir,id = id)

    
    return render(request,"detail.html",{"yapbitir" : yapbitir})

@login_required(login_url="user:login")
def updateYapbitir(request,id):

    yapbitir = get_object_or_404(Yapbitir,id = id,author = request.user)
    form = YapbitirForm(request.POST or None , request.FILES or None, instance= yapbitir)
    
    if form.is_valid():
        yapbitir = form.save(commit=False)
        yapbitir.author = request.user
        yapbitir.save()

        messages.success(request,"Liste Başarıyla Güncellendi...")
        return redirect("yapbitir:dashboard")
    return render(request,"update.html", {"form": form})


@login_required(login_url="user:login")
def deleteYapbitir(request,id):
    yapbitir = get_object_or_404(Yapbitir,id=id,author = request.user)
    yapbitir.delete()

    messages.success(request,"Liste Başarıyla Silindi...")
    return redirect("yapbitir:dashboard")


def yes_finish(request,id):
    yapbitir = Yapbitir.objects.get(pk=id)
    yapbitir.finished = False
    yapbitir.save()
    return redirect("yapbitir:dashboard")

def no_finish(request,id):
    yapbitir = Yapbitir.objects.get(pk=id)
    yapbitir.finished = True  
    yapbitir.save()
    return redirect("yapbitir:dashboard")
