from django.conf.urls import url, include
from .views import populate, display

urlpatterns = [
    url('^populate/$', populate),
    url('^display/$', display)
]
