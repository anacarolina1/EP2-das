from django.conf.urls import url
from . import views
from django.dispatch import receiver

urlpatterns = [
    url(r'^$', views.home, name='home'),

]