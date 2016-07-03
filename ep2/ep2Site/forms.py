from django import forms

from .models import Musica, Review

class MusicaForm(forms.ModelForm):
	model = Musica
	fields = ('nome', 'url')

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('musica', 'data_pub', 'nome_de_usuario', 'comentario', 'rating')
        widgets = {
        	'musica' = forms.TextInput(attrs={'class': 'form-control'})
        	'data_pub' = forms.TextInput(attrs={'class': 'form-control'}),
        	'nome_de_usuario' = forms.TextInput(attrs={'class': 'form-control'}),
        	'comentario' = forms.TextInput(attrs={'class': 'form-control'}),
        	'rating' = forms.Select(attrs={'class': 'dropdown form-control'}, choices=RATING_CHOICES),
        }