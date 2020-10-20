from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(request):
	return HttpResponse("Hello puto");


def detail(request, question_id):
	ret