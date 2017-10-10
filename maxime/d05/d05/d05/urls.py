from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	url(r'^ex00/', include('ex00.urls')),
	url(r'^ex01/', include('ex01.urls')),
	url(r'^ex02/', include('ex02.urls')),
	url(r'^ex03/', include('ex03.urls')),
    url(r'^admin/', admin.site.urls),
]
