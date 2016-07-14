from django.shortcuts import render
from forms import ReviewForm
import twitter
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView, CreateView
from models import Review
from django.core.urlresolvers import reverse_lazy

   
class Home(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        return render(request, 'ep2Site/home.html')


def review(request):

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.save() 
            return music(request)
          
    else:
        form = ReviewForm()

    return render_to_response('ep2Site/review.html',
            {'form': form}, context_instance=RequestContext(request))


def music(request):
    form = ReviewForm
    return render(request, 'ep2Site/review.html', {'form': form})

class Register(CreateView):
    template_name = 'review.html'
    fields = ['musica', 'data_lancamento', 'nome_de_usuario', 'review', 'rating', 'url']
    model = Review
    success_url = reverse_lazy('list')

class List(ListView):
    template_name = 'home.html'
    model = Review
    context_object = 'name'


def videos(request):
     return render(request, 'ep2Site/videos.html')










#context['tweets'] = get_tweets()