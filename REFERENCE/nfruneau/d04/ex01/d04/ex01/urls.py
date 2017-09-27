from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'django', views.django, name='django'),
    url(r'affichage', views.affichage, name='affichage'),
    url(r'templates', views.templates, name='templates'),
]
