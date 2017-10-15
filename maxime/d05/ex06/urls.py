from django.conf.urls import url, include
from .views import populate, display, update, init

app_name = 'ex06'
urlpatterns = [
    url('^init/$', init),
    url('^populate/$', populate),
    url('^display/$', display),
    url('^update/$', update, name='update'),
]
