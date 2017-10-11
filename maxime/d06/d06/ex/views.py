from django.shortcuts import render, redirect
from django.conf import settings
from ex.forms import FormSign
import random

# https://stackoverflow.com/questions/1622793/django-cookies-how-can-i-set-them/5575578#5575578

def index(request):
	names = settings.TOURISTS
	value = random.choice(names)
	key = 'tourist_name'
	if key not in request.COOKIES:
		request.COOKIES[key] = value
		response = render(request, 'ex/index.html')
		response.set_cookie(key, value, max_age=42)
	else:
		response = render(request, 'ex/index.html')
	return response


def signin(request):
	if request.method == "POST":
		form = FormSign(request.POST)
		if form.is_valid(): # a partir d'ici, c'est pas bon
			readform(form)
			form.save()
			return redirect('/')
	else:
		form = FormSign()
	return render(request, 'ex/signin.html', {'form': form})


def readform(form):
	different = False if form['password'] == form['password_check'] else True
	for field in form:
		print(field.value())
	return different
