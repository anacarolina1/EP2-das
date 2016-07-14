from django.conf.urls import url
from . import views
from django.dispatch import receiver
from django.contrib import admin


urlpatterns = [
	url(r'^home', views.Home.as_view(), name='home'),
    url(r'^review', views.review, name='review'),
    url(r'^videos', views.videos, name='review'),
]

