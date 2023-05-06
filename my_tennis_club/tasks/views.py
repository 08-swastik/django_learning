from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse


class NewTaskForm(forms.Form) :
    task = forms.CharField(label="New Task")

tasks = ["swastik"]
# Create your views here.
def index(request):
    return render(request,"tasks/index.html",
                  {"tasks":tasks
                   }) #we have access to the variable key tasks which the templates will render and display the tasks
def create(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)

        if form.is_valid() :
            task = form.cleaned_data["task"]
            tasks.append(task)
            #return HttpResponseRedirect(reverse("tasks:index.html"))
            return redirect('tasks:index')

        else:
            return render(request,"tasks/create.html",{"form":form})

    return render(request,"tasks/create.html",{
        "form" : NewTaskForm()
    })