from django.contrib import admin

from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ['musica', 'url', 'data_lancamento', 'nome_de_usuario', 'comentario', 'rating']
    list_filter = ['nome_de_usuario']
    search_fields = ['comentario']

admin.site.register(Review, ReviewAdmin)