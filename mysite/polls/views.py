from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello Viewer , You'r at the polls index")

def detail(request,question_id):
    return HttpResponse(f"You're looking at question {question_id}.")


