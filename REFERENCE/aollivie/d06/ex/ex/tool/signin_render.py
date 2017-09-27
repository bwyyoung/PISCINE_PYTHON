from .Rendu import Rendu
from django.shortcuts import render, HttpResponse, redirect
from ..models import MyUser
from .MyUserForm import MyUserForm
from django.contrib import auth

def signin_render(request):
    err = 0
    if request.user and request.user.is_authenticated:
        return redirect('/')
    r = Rendu(request)
    if request.method == 'POST':
        form = MyUserForm(request.POST)
        err = form.is_valid()
        if (err  == 0 ):
            u = MyUser.objects.create_user(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            u.is_active = True
            u.save()
            user = auth.authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user and user.is_active:
                auth.login(request, user)
                return redirect('/')
            return r.do_render()
        else:
            if err == 1:
                r.error = 'Username already exist'
            else:
                r.error = 'Same password required'
            r.do_form_user()
    else:
        r.do_form_user()

    return r.do_render()
