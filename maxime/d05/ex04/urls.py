from django.conf.urls import url, include
from .views import populate, display, remove, init

app_name = 'ex04'
urlpatterns = [
    url('^init/$', init),
    url('^populate/$', populate),
    url('^display/$', display),
    url('^remove/$', remove, name='remove'),
]
