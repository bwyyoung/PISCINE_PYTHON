from . import elements as e
from .elem import Text
from django.conf import settings
import random
from django.shortcuts import render, HttpResponse
from ..models import MyUser
from ..models import Tip
from .MyUserForm import MyUserForm
from .LoginForm import LoginForm
from .TipForm import TipForm
import ast


class Rendu:
    """docstring for Rendu."""
    def __init__(self, request, template='ex/base.html'):
        self.request = request
        self.error = None
        self.is_new_cookie = True
        self.cookie_name = 'mycookie'
        self.set_cookie()
        self.nav = self.do_nav()
        self.template = template
        self.form = None
        self.form_user = None
        self.form_login = None
        self.form_tip = None
        self.tips = None

    def set_cookie(self):
        v_cookie = ''
        if self.request.user and self.request.user.is_authenticated:
            self.is_new_cookie = True
            self.request.COOKIES[self.cookie_name] = self.request.user
        if self.cookie_name in self.request.COOKIES:
            self.is_new_cookie = False
        else:
            r = random.randrange(0, len(settings.NAME))
            v_cookie = settings.NAME[r]
            self.request.COOKIES[self.cookie_name] = v_cookie
            self.is_new_cookie = True

    def do_nav(self):
        content = []
        cookie_name = 'Hello '
        cookie_name += str(self.request.COOKIES[self.cookie_name])
        cookie_name += ' !'
        content.append(e.Div(Text(cookie_name)))

        content.append(e.A(Text('Home'), attr={'href': 'http://127.0.0.1:8000/'}))
        if self.request.user and self.request.user.is_authenticated:
            content.append(e.A(Text('Logout'), attr={'href': 'http://127.0.0.1:8000/logout'}))
        else:
            content.append(e.A(Text('Signin'), attr={'href': 'http://127.0.0.1:8000/signin'}))
            content.append(e.A(Text('Login'), attr={'href': 'http://127.0.0.1:8000/login'}))
        nav = e.Nav(content)
        return nav

    def do_render(self):
        rendu = {}
        rendu['nav'] = self.nav
        if self.form != None:
            rendu['form'] = self.form
        if self.error:
            rendu['error'] = self.error
        if self.tips:
            content = []
            input_field = Text('')
            for v in self.tips:



                if v.downvotes != None :
                    nb_down = len(ast.literal_eval(v.downvotes))
                else:
                    nb_down = 0
                if self.request.user and self.request.user.is_authenticated:
                    input_field = []
                    input_field.append(e.Input(Text('Delete') , attr={'type':'submit', 'name':str(v.id), 'value':'Delete'}))
                    input_field.append(e.Input(Text('Upvote') , attr={'type':'submit', 'name':str(v.id), 'value':'Upvote'}))
                    input_field.append(e.Input(Text('Downvote') , attr={'type':'submit', 'name':str(v.id), 'value':'Downvote'}))
                    input_field = e.Div(input_field)
                else:
                    input_field=e.Text('')
                content.append(e.Div( [e.Span(Text(v.contenu)), e.Span(Text(v.auteur)), e.Span(Text(str(v.date))), e.Span(Text(str(nb_down))) , input_field], attr={'style':'border: solid 1px red;' }) )
            rendu['tips'] = e.Div(content)
        if self.is_new_cookie:
            response = render(self.request, self.template, rendu)
            response.set_cookie(self.cookie_name, self.request.COOKIES[self.cookie_name], settings.SESSION_COOKIE_AGE)
            return response
        return render(self.request, self.template, rendu)

    def do_form_user(self):
        self.form_user = MyUserForm()
        self.form = self.form_user
        self.template = 'ex/form.html'

    def do_form_login(self):
        self.form_login = LoginForm()
        self.form = self.form_login
        self.template = 'ex/form.html'

    def do_form_tip(self):
        self.form_tip = TipForm()
        self.form = self.form_tip
        self.template = 'ex/form.html'

    def do_tip_list(self):
        tips = Tip.objects.all()
        self.tips = tips
