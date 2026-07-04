from django.urls import path 
from . import views 

urlpatterns = [
    path("",views.index,name = "index "),# when url is empty call views.index
    path("<int:question_id>/",views.detail,name="detail"), 
]

