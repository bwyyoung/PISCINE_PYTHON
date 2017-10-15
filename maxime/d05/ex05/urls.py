from django.conf.urls import url, include
from .views import populate, display, remove

app_name = 'ex05'
urlpatterns = [
    url('^populate/$', populate),
    url('^display/$', display),
    url('^remove/$', remove, name='remove'),
]
