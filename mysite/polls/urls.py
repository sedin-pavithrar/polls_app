from django.urls import path 
from . import views 

urlpatterns = [
    path("",views.index,name = "index ") # when url is empty call views.index 
]

