from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.



def index(request):
    d={
        'data':port.objects.all()
    }
    if request.method =="POST":
        name =request.POST.get('name')
        email =request.POST.get('email')
        numb =request.POST.get('number')
        mesg =request.POST.get('msg')

        ob=formdata(uname=name,em=email,num=numb,feedback=mesg)
        ob.save()
        return render(request,'index.html')
    return render(request,'index.html',d)
    
