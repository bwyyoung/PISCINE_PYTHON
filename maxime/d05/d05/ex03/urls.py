from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='init'),
	url(r'^populate/$', views.populate, name='populate'),
	# url(r'^remove/$', views.remove, name='remove'),
	url(r'^display/$', views.display, name='display'),
]
