from __future__ import absolute_import

from django.conf.urls import url
from django.core.urlresolvers import reverse

from djangoplugins.point import PluginPoint

import ep2Site.views


class ContentType(PluginPoint):
    urls = [
        url(r'^$', ep2Site.views.content_list, name='home'),
        url(r'^create/$', ep2Site.views.content_create,
            name='content-create')
    ]


    def get_list_url(self):
        return reverse('home')

    def get_create_url(self):
        return reverse('review')

    def get_read_url(self, content):
        return reverse('content-read', args=[content.pk])