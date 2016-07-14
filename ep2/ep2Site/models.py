from django.db import models


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

    def __unicode__(self):
        return self.musica



