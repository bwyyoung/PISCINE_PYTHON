from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^login/$', views.Login.as_view(), name="myauth-login"),
    url(r'^logout/$', login_required(views.Logout.as_view()), name="myauth-logout"),
    url(r'^register/$', views.Register.as_view(), name="myauth-register"),
]
