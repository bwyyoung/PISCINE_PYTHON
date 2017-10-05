from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse_lazy
from django.utils.http import is_safe_url
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import FormView, RedirectView
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.utils import timezone
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from django.contrib.auth.views import logout
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.forms import widgets
from django import forms

from .models import Article, UserFavouriteArticle

from .PublishForm import PublishForm
from .models import Article

# Create your views here.

class LoginView(FormView):
    """
    Provides the ability to login as a user with a username and password
    """
    success_url = reverse_lazy('home')
    form_class = AuthenticationForm
    redirect_field_name = REDIRECT_FIELD_NAME

    @method_decorator(sensitive_post_parameters('password'))
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        # Sets a test cookie to make sure the user has cookies enabled
        request.session.set_test_cookie()

        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        auth_login(self.request, form.get_user())

        # login
        # If the test cookie worked, go ahead and
        # delete it since its no longer needed
        if self.request.session.test_cookie_worked():
            self.request.session.delete_test_cookie()

        return super(LoginView, self).form_valid(form)

    def get_success_url(self):
        redirect_to = self.request.GET.get(self.redirect_field_name)
        if not is_safe_url(url=redirect_to, host=self.request.get_host()):
            redirect_to = self.success_url
        return redirect_to

class LogoutView(RedirectView):
    """
    Provides users the ability to logout
    """
    url = reverse_lazy('home')
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        print('logout !!!!!!!!!!!!!')
        auth_logout(request)
        # logout(request)
        # print('logout')
        return super(LogoutView, self).get(request, *args, **kwargs)

class RegistrationView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)




# @login_required(login_url=reverse_lazy('login'))
class PublishView(CreateView):
    model = Article
    fields = ['title', 'content', 'synopsis',]
    # form_class = PublishForm
    success_url = reverse_lazy('home')
    user = None
    def form_valid(self, form):
        article = form.save(commit=False)

        user = User.objects.get(username=self.request.user.username)

        article.author = user

        article.save()
        return super().form_valid(form)

class AddFavouritView(CreateView):
    model = UserFavouriteArticle
    fields = []
    # form_class = PublishForm
    success_url = reverse_lazy('home')
    user = None
    def form_valid(self, form):
        article = form.save(commit=False)

        user = User.objects.get(username=self.request.user.username)

        article.user = user
        article.article = Article.objects.get(id=self.kwargs['title'])
        article.save()
        return super().form_valid(form)





class ArticleListView(ListView):
    model = Article
    def __init__(self, **kwargs):
        super(ArticleListView, self).__init__(**kwargs)
        try:
            # User.objects.all().delete()
            # Article.objects.all().delete()
            usera = User.objects.create_user(username='a',
                                     email=None,
                                     password='a')
            usera.save()
            userb = User.objects.create_user(username='b',
                                     email=None,
                                     password='b')
            userb.save()
            userc = User.objects.create_user(username='c',
                                     email=None,
                                     password='c')
            userc.save()
            userd = User.objects.create_user(username='d',
                                     email=None,
                                     password='d')
            userd.save()
            usere = User.objects.create_user(username='e',
                                     email=None,
                                     password='e')

            usere.save()
            articlea = Article(title='A',
                                     author=usera,
                                     synopsis='aa',
                                     content='aaaaaaaa')
            articlea.save()
            articleb = Article(title='B',
                                     author=userb,
                                     synopsis='bb',
                                     content='bbbbbbbbbb')
            articleb.save()
            articlec = Article(title='C',
                                     author=userc,
                                     synopsis='cc',
                                     content='ccccccc')
            articlec.save()
            articled = Article(title='D',
                                     author=userd,
                                     synopsis='dd',
                                     content='ddddddddd')
            articled.save()
            articlee = Article(title='E',
                                     author=usere,
                                     synopsis='ee',
                                     content='eeeeeee')
            articlee.save()
            fab = UserFavouriteArticle(user=usera, article=articleb)
            fab.save()
            fac = UserFavouriteArticle(user=usera, article=articlec)
            fac.save()
        except Exception as e:
            print(e)

    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class PublicationsListView(ListView):

    def __init__(self, **kwargs):
        super(PublicationsListView, self).__init__(**kwargs)

    def get(self, request):
        print('GET !!!!!!!!!!')
        print(request.user.is_authenticated())
        print(request.user.username)
        user = User.objects.filter(username=request.user.username)
        self.queryset = Article.objects.filter(author=user)
        return super(PublicationsListView, self).get(request)

    def get_context_data(self, **kwargs):
        context = super(PublicationsListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class FavouritesListView(ListView):

    def __init__(self, **kwargs):
        super(FavouritesListView, self).__init__(**kwargs)

    def get(self, request):
        print('GET !!!!!!!!!!')
        print(request.user.is_authenticated())
        print(request.user.username)
        user = User.objects.filter(username=request.user.username)
        self.queryset = UserFavouriteArticle.objects.filter(user=user)
        return super(FavouritesListView, self).get(request)

    def get_context_data(self, **kwargs):
        context = super(FavouritesListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class ArticleDetailView(DetailView):
    model = Article
    slug_field = 'title'
    slug_url_kwarg = 'title'

    def get_context_data(self, **kwargs):
        # print('article:', **kwargs)
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

def home(request):
    return redirect(reverse_lazy('article_list'))

def publications(request):
    return HttpResponse('publications')

def detail(request):
    return HttpResponse('detail')
