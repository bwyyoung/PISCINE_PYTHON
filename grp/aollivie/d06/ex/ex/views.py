from django.shortcuts import render, HttpResponse
from .tool.home_render import home_render
from .tool.signin_render import signin_render
from .tool.login_render import login_render, logout_render
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return home_render(request)


def signin(request):
    return signin_render(request)

def login(request):
    return login_render(request)

@login_required
def logout(request):
    return logout_render(request)
