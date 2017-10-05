from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^inscription$', views.inscription),
    url(r'^connexion$', views.connexion),
    url(r'^logout$', views.logout),
]
