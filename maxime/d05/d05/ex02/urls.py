from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^init/$', views.init, name='init'),
	url(r'^populate/$', views.populate, name='populate'),
	url(r'^display/$', views.display, name='display'),
	url(r'^remove/$', views.remove, name='remove'),
]
