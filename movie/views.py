from django.shortcuts import render,get_list_or_404,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms  import *

# Create your views here.

@login_required(login_url='/user/login/')
def otelEkle(request):
    if request.method=='POST':
        form = FormOlustur(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('detay1')
        else:
            return render(request,'otel-ekle.html',{'form':form})
    form = FormOlustur()
    return render(request,'otel-ekle.html',{'form':form})

def tesisEkle(request):
    if request.method=='POST':
        form = TesisOlustur(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('base')
        else:
            return render(request,'tesis-ekle.html',{'form':form})
    form = TesisOlustur()
    return render(request,'tesis-ekle.html',{'form':form})
