from django.shortcuts import HttpResponse, render, redirect
from django.conf import settings
from django.contrib import auth
from django.contrib.auth.models import User
from .forms import LoginForm, SigninForm, TipForm
from my_app.models import Tip
import random
from datetime import datetime

# Create your views here.

def index(request):
	try:
		if request.user.is_authenticated():
			if request.method == 'POST':
				form = TipForm(request.POST)
				if form.is_valid():
					content = form.cleaned_data['content']
					curr = request.user
					author = curr.username
					postdate = datetime.now()
					t = Tip(content=content, author=author)
					t.save()
			else:
				form = TipForm()
			p = Tip.objects.all()
			print(p)
			l = []
			for row in p:
				lr = (row.content, row.author, row.postdate)
				l.append(lr)
			return render(request, "my_app/index.html", {'form':form, 'data':l})
		p = Tip.objects.all()
		l = []
		for row in p:
			lr = (row.content, row.author, row.postdate)
			l.append(lr)
		if 'mycookie' not in request.COOKIES:
			cookie = random.choice(settings.NAME_LIST)
			request.COOKIES['mycookie'] = cookie
			response = render(request, "my_app/index.html", {'data':l})
			response.set_cookie('mycookie', cookie, max_age=settings.SESSION_COOKIE_AGE)
			return response
	except Exception as e:
		return HttpResponse (e)
	return render(request, "my_app/index.html", {'data':l})

def inscription(request):
	try:
		if request.user.is_authenticated():
			return redirect('/')
		if request.method == 'POST':
			form = SigninForm(request.POST)
			if form.is_valid():
				username = form.cleaned_data['username']
				password1 = form.cleaned_data['password1']
				password2 = form.cleaned_data['password2']
				if not password2:
				    raise Exception ("You must confirm your password")
				if password1 != password2:
				    raise Exception ("Your passwords do not match")
				user = User.objects.create_user(username, None, password1)
				if user and user.is_active:
					auth.login(request, user)
					return redirect('/')
				else:
					form._errors['username'] = ["Wrong username or password"]
		else:
			form = SigninForm()
		err = None
	except Exception as e:
		err = str(e)
	print(err)
	return render(request, "my_app/inscription.html", {'form':form, 'error':err})

def connexion(request):
	if request.user.is_authenticated():
		return redirect('/')
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = auth.authenticate(username=username, password=password)
			if user and user.is_active:
				auth.login(request, user)
				return redirect('/')
			else:
				form._errors['username'] = ["Wrong username or password"]
	else:
		form = LoginForm()
	return render(request, "my_app/connexion.html", {'form':form})

def logout(request):
	auth.logout(request)
	return redirect('/')
