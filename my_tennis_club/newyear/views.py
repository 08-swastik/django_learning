from django.shortcuts import render
import datetime
# Create your views here.
def index(request):
    now = datetime.datetime.now()
    return render(request  ,"newyear/index.html",{
        "newyear" : now.month ==1 and now.date == 1 #newyear stores the value as boolean true or false.if true the if line executes in html and so on.
        
    })