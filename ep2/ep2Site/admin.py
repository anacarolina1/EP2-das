from django.contrib import admin

from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    model = Review
    lista = ('musica', 'url', 'data_lancamento', 'nome_de_usuario', 'comentario', 'rating')
    lista_filtro = ['nome_de_usuario']
    procurar = ['comentario']

admin.site.register(Review, ReviewAdmin)