from django.contrib import admin

from .models import Musica, Review

class ReviewAdmin(admin.ModelAdmin):
    model = Review
    lista = ('musica', 'rating', 'nome_de_usuario', 'commentario', 'data_pub')
    lista_filtro = ['data_pub', 'nome_de_usuario']
    procurar = ['commentario']

admin.site.register(Musica)
admin.site.register(Review, ReviewAdmin)