from django.shortcuts import render, HttpResponse
import psycopg2

def index(request):
	return HttpResponse("ex01")
