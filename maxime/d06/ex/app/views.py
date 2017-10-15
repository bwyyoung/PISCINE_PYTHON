from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.conf import settings
from .forms import RegisterForm, LoginForm, TipForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import Tip
import random

@login_required
def up(request, tip_id=None):
    obj = get_object_or_404(Tip, id=tip_id)
    obj.downvotes.remove(request.user)
    if request.user in obj.upvotes.all():
        obj.upvotes.remove(request.user)
    else:
        obj.upvotes.add(request.user)
    return redirect('/')


@login_required
def down(request, tip_id=None):
    obj = get_object_or_404(Tip, id=tip_id)
    if obj.auteur == request.user or request.user.has_perm('app.downvote_tip'):
        obj.upvotes.remove(request.user)
        if request.user in obj.downvotes.all():
            obj.downvotes.remove(request.user)
        else:
            obj.downvotes.add(request.user)
    return redirect('/')

@login_required    
def delete(request, tip_id=None):

    obj = get_object_or_404(Tip, id=tip_id)
    if obj.auteur == request.user or request.user.has_perm('app.delete_tip'):
        obj.delete()
    return redirect('/')



@login_required
def create(request):
    if request.method == 'POST':
        form = TipForm(request.POST)
        if form.is_valid():
            o = Tip(auteur=request.user, contenu=form.cleaned_data['contenu'])
            o.save()
            return redirect('/')
        else:
            home(request, form)
    return redirect('/')

def home(request, form=None):

    cookie = request.COOKIES.get('anon_auth', None)
    if not cookie:
        cookie = random.choice(settings.RANDOM_NAMES)
        request.COOKIES['anon_auth'] = cookie
        response = render(request, "app/base.html", {})
        response.set_cookie('anon_auth', cookie, max_age=42)
        return response
    else:
        return render(request, "app/home.html", {
            'queryset': Tip.objects.all(),
            'form': TipForm() if not form else form
        })

def logout(request):

    auth.logout(request)
    return redirect('/')

def login(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            auth.login(request, form.cleaned_data['user'])
            return redirect('/')
    else:
        form = LoginForm()
    return render(request, "app/login.html", {'form': form})

def register(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            u = form.save()
            auth.login(request, u)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, "app/register.html", {'form': form})
