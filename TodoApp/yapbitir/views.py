from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,"index.html")
#htmle veri göndermek için render fonk kullanılabilir!SÖZLÜK YAPISI OLMASI KOŞULU İLE

def about(request):
    return render(request,"about.html")

def yapbitirs(request):
    return render(request,"yapbitirs.html")