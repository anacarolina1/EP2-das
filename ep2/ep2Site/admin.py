from django.contrib import admin

from .models import Review
from embed_video.admin import AdminVideoMixin


class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ['musica', 'url', 'data_lancamento', 'nome_de_usuario', 'review', 'rating']
    list_filter = ['nome_de_usuario']
    search_fields = ['review']

admin.site.register(Review, ReviewAdmin)


