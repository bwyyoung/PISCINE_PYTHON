from .Rendu import Rendu
from django.contrib import auth
from django.shortcuts import render, HttpResponse, redirect
from .LoginForm import LoginForm

def login_render(request):
    if request.user and request.user.is_authenticated:
        return redirect('/')
    r = Rendu(request)
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return redirect('/')
            r.error = 'Bad couple username and password'
            r.do_form_login()
            return r.do_render()
        else:
            r.do_form_login()
    else:
        r.do_form_login()
    return r.do_render()

def logout_render(request):
    auth.logout(request)
    return redirect('/')
