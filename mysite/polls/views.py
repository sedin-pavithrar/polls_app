from django.shortcuts import render
from django.http import HttpResponse

from .models import Question
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5] #querying the db 
    #question.objects -> question table slice 5 -newest first 

    context = {
        "latest_question_list": latest_question_list
    } 

    return render(request,"polls/index.html",context)
   # render needs three things 
   # Request - > who asked 
   # Template -> Which HTML file 
   # Context -> What data should appear 

    # return HttpResponse("Hello Viewer , You'r at the polls index")

def detail(request,question_id):
    return HttpResponse(f"You're looking at question {question_id}.")

def result(request,question_id):
    return HttpResponse(f"You're looking at the results of question {question_id}.")

def vote(request,question_id):
    return HttpResponse(f"You're voting on question {question_id}.")


