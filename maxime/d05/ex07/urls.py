from django.conf.urls import url, include
from .views import populate, display, update

app_name = 'ex07'
urlpatterns = [
    url('^populate/$', populate),
    url('^display/$', display),
    url('^update/$', update, name='update'),
]
