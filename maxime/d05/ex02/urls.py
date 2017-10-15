from django.conf.urls import url, include
from .views import populate, display, init

urlpatterns = [
    url('^init/$', init),
    url('^populate/$', populate),
    url('^display/$', display)
]
