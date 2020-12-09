from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def CurrentDate(request):
   date=datetime.datetime.now()
   h=int(date.strftime("%H"))
   msg='<h1>Hello Guest very '
   if h<12:
       msg=msg+'Good Morning'
   elif h<16:
       msg=msg+'Good Afternoon'
   elif h<20:
       msg=msg+'Good Evening'
   else:
       msg=msg+'Good night'
   msg=msg+'</h1><hr>'
   msg=msg+'<h1> Now current time is:'+str(date)+'</h1>'

   return HttpResponse(msg)

def punejobinfo(request):
    s="<h1>Here...All info about punejobs</h1>"
    return HttpResponse(s)

def mumbaijobinfo(request):
    s="<h1>Here...All info about Mumbaijobs</h1>"
    return HttpResponse(s)

def chennaijobinfo(request):
    s="<h1>Here...All info about Chennaijobs</h1>"
    return HttpResponse(s)