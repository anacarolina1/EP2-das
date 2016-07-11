from django.conf.urls import url
from . import views
from django.dispatch import receiver

urlpatterns = [
	url(r'^home', views.Home.as_view(), name='home'),
    url(r'^review', views.review, name='review'),

]