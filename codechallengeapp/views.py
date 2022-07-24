from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import bottom


def demo(request):
   obj=Place.objects.all()
   obj1 = bottom.objects.all()
   return render(request,"index.html" ,{'result':obj,'result1':obj1})








# def output(request):
#    x=int(request.GET['num1'])
#    y=int(request.GET['num2'])
#    add=x+y
#    Mul=x*y
#    sub=x-y
#    div=x/y


  # return render(request,"output.html", {'add':add,'Mul':Mul,'sub':sub,'div':div})



