from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', login_required(views.Home.as_view()), name="forum-home"),
    url(r'^posts/$', login_required(views.PostList.as_view()), name="forum-posts"),
    url(r'^detail/(?P<pk>[0-9]+)/$', login_required(views.PostView.as_view()), name="forum-detail"),
    url(r'^publish/$', login_required(views.PostForm.as_view()), name="forum-publish"),
    url(r'^comment/(?P<p_pk>[0-9]+)/$', login_required(views.Comment.as_view()), name="forum-comment"),
]
