from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', login_required(views.UserProfileDetail.as_view()), name="userprofile-home"),
    url(r'^edit/(?P<pk>[0-9]+)/$', login_required(views.UserProfileEdit.as_view()), name="userprofile-edit"),
    url(r'^addgroup/(?P<pk>[0-9]+)/$', login_required(views.add_privileges), name="userprofile-addgroup"),
    url(r'^removegroup/(?P<pk>[0-9]+)/$', login_required(views.remove_privileges), name="userprofile-removegroup"),
]
