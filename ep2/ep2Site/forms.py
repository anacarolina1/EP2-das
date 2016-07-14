from django import forms

from .models import Review

RATING_CHOICES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
)

class ReviewForm(forms.ModelForm):


    class Meta:
    	model = Review
        fields = ('musica', 'data_lancamento', 'nome_de_usuario', 'review', 'rating', 'url')
        widgets = {
            'nome_de_usuario': forms.TextInput(attrs={'class': 'form-control'}),
        	'musica': forms.TextInput(attrs={'class': 'form-control'}),
            'url': forms.TextInput(attrs={'class': 'form-control'}),
        	'data_lancamento': forms.TextInput(attrs={'class': 'form-control'}),
        	'review': forms.TextInput(attrs={'class': 'form-control'}),
        	'rating': forms.Select(attrs={'class': 'dropdown form-control'}, choices=RATING_CHOICES),
        }

