"""d07 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^logout/?$', views.LogoutView.as_view(), name='logout'),
    url(r'^login/?$', views.LoginView.as_view(template_name='ex/login.html'), name='login'),
    url(r'^register/?$', views.RegistrationView.as_view(template_name='ex/register.html'), name='register'),
    url(r'^articles/?$', views.ArticleListView.as_view(template_name='ex/article_list.html'), name='article_list'),
    url(r'^publications/?$', login_required( views.PublicationsListView.as_view(template_name='ex/publications_list.html')), name='publications_list'),
    url(r'^favourites/?$', views.FavouritesListView.as_view(template_name='ex/favourites_list.html'), name='favourites_list'),
    url(r'^publish/?$', login_required( views.PublishView.as_view(template_name='ex/publish.html')), name='publish'),
    url(r'^add_favourite/(?P<title>[-\w]+)/?$', login_required( views.AddFavouritView.as_view(template_name='ex/add.html')), name='add'),
    url(r'^$', views.home, name='home'),
    url(r'^detail/(?P<title>[-\w]+)/?$', views.ArticleDetailView.as_view(template_name='ex/article_detail.html'), name='detail'),

]
