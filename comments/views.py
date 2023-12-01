from django.shortcuts import render,redirect
from .models import *
from .forms  import *

# Create your views here.

# @login_required(login_url='/user/login/')
def yorumEkle(request):
    if request.method=='POST':
        form = YorumOlustur(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('detay2')
        else:
            return render(request,'yorum-ekle.html',{'form':form})
    form = YorumOlustur()
    return render(request,'yorum-ekle.html',{'form':form})
