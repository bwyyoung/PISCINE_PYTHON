from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello World !")

def base(request):
	return render(request, "ex01/base.html")

def django(request):
	return render(request, "ex01/django.html")

def affichage(request):
	return render(request, "ex01/affichage.html")

def templates(request):
	return render(request, "ex01/templates.html")
