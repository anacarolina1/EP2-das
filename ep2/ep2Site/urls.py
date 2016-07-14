from django.conf.urls import url
from . import views
from django.dispatch import receiver
from django.contrib import admin
from djangoplugins.utils import include_plugins
from .plugins import ContentType



urlpatterns = [
	url(r'^home', views.Home.as_view(), name='home'),
    url(r'^review', views.review, name='review'),
    url(r'^videos', views.videos, name='review'),
    url(r'^review/', include_plugins(ContentType)),
    url(r'^review/', include_plugins(
        ContentType, '{plugin}/(?P<pk>\d+)/', 'instance_urls'
    )),
]

