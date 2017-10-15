from django.conf.urls import url
from .views import home, login, logout, register, create, up, down, delete


app_name="app"
urlpatterns = [
    url(r'^$', home, name="home"),
    url(r'^register/$', register, name="register"),
    url(r'^login/$', login, name="login"),
    url(r'^logout/$', logout, name="logout"),
    url(r'^create/$', create, name="create"),
    url(r'^up/(?P<tip_id>[0-9]+)/$', up, name="up"),
    url(r'^down/(?P<tip_id>[0-9]+)/$', down, name="down"),
    url(r'^delete/(?P<tip_id>[0-9]+)/$', delete, name="delete")
]
