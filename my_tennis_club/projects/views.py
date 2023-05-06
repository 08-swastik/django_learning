from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse #import the ability to use http response

def projects(request,name):
    return render(request,"projects/projects.html",{"name":name.capitalize()}) #we are passing the name as variable(key) to the html file and its value is ..
#we have written a view which accepts request and displays hhtp response through the class

def index(request):
    return render(request,"projects/index.html")