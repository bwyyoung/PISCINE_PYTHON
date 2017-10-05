from django.shortcuts import HttpResponse, render, redirect
from my_app.models import Article, UserFavouriteArticle
from django.views.generic import ListView, FormView, DetailView, RedirectView
from django.contrib.auth.forms import AuthenticationForm

class home(RedirectView):
	 pattern_name = '/articles'

class login(FormView):
	form_class = AuthenticationForm
	template_name = "my_app/login.html"
	success_url = "/"

class articles(ListView):
	model = Article
	template_name = "my_app/articles.html"

class publications(ListView):
	template_name = "my_app/publications.html"
	context_object_name = 'author'
	queryset = Article.objects.all()

class detail(DetailView):
	model = Article
	template_name = "my_app/detail.html"

class logout(RedirectView):
	# logout
	 pattern_name = '/articles'

class favourites(ListView):
	model = Article
	template_name = "my_app/favourites.html"
