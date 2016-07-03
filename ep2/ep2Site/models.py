from django.db import models

class Musica(models.Model):
    nome = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
           
    def __unicode__(self):
        return self.nome


class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    musica = models.ForeignKey(Musica)
    data_pub = models.DateTimeField('data de publicacao')
    nome_de_usuario = models.CharField(max_length=100)
    comentario = models.CharField(max_length=200)
    rating = models.IntegerField(choices=RATING_CHOICES)
    