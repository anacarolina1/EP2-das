from __future__ import absolute_import
from django.db import models
from djangoplugins.fields import PluginField

from ep2Site.plugins import ContentType


class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    nome_de_usuario = models.CharField(max_length=200)
    musica = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    data_lancamento = models.DateTimeField('data de lancamento')
    review = models.CharField(max_length=200)
    rating = models.IntegerField(choices=RATING_CHOICES)
    plugin = PluginField(ContentType, editable=False)

    def __unicode__(self):
        return self.musica

    def get_absolute_url(self):
        return self.plugin.get_plugin().get_read_url(self)



