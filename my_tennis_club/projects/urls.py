from django.urls import path
from . import views #to use the views file ,we have to import it from views.py in the current directory

urlpatterns = [
    path('', views.index , name="index"),#two arguments
    path('<str:name>',views.projects, name= "projects"),
    
]
#the above two routes the single quote will trigger the projects function.