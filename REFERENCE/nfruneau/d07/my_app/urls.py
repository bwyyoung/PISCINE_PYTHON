from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^login$', views.login.as_view()),
    url(r'^articles$', views.articles.as_view()),
    url(r'^publications$', views.articles.as_view()),
    url(r'^detail/(?P<pk>[0-9]+)', views.detail.as_view(), name="page_detail"),
    url(r'^logout$', views.articles.as_view()),
    url(r'^favourites$', views.articles.as_view()),
]
