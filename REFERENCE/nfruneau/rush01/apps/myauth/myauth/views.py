from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.urlresolvers import reverse_lazy
from django.contrib import auth
from django.core.urlresolvers import reverse
from django.views.generic import ListView, RedirectView, FormView, DetailView, CreateView
from django.conf import settings


class Login(FormView):
	template_name = 'myauth/login.html'
	form_class = AuthenticationForm
	success_url = reverse_lazy('home')

	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			return redirect(self.success_url)
		else:
			return super(Login, self).get(request, *args, **kwargs)

	def form_valid(self, form):
		user = form.get_user()
		if user and user.is_active:
			auth.login(self.request, user)
		return super(Login, self).form_valid(form)

class Logout(RedirectView):
	pattern_name = 'home'

	def get(self, request, *args, **kwargs):
		auth.logout(request)
		return super(Logout, self).get(request, *args, **kwargs)

class Register(CreateView):
	model = auth.models.User
	form_class = UserCreationForm
	template_name = 'myauth/user_form.html'
	success_url = reverse_lazy('home')

	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			return redirect(self.success_url)
		else:
			return super(Register, self).get(request, *args, **kwargs)

	def form_valid(self, form):
		user = form.save()
		auth.login(self.request, user)
		return redirect(self.success_url)
