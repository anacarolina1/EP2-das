from django.shortcuts import render
from forms import ReviewForm
import twitter
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView, CreateView
from models import Review
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
import ep2plugin

   
class Home(TemplateView):
    template_name = 'home.html'


    def review_list(request, plugin):
        return render(request, 'ep2Site/home.html', {
            'plugin': ep2Site.plugins.reviewType.get_plugin(plugin),
            'post': ep2Site.models.Review.objects.all(),
        })



def review(request):

    import ep2Site.models

    plugin = ep2Site.plugins.reviewType.get_plugin(plugin)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.plugin = plugin.get_model()
            review.save() 
            return HttpResponseRedirect(review.get_absolute_url())
        else:
            return "[ERROR] from views: {0}".format(form.errors)
          
    else:
        form = ep2Site.forms.ReviewForm()

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


def review_read(request, pk, plugin):
    plugin = ep2Site.plugins.reviewType.get_plugin(plugin)
    review = get_object_or_404(ep2Site.models.review,
                                pk=pk, plugin=plugin.get_model())
    return render(request, 'review/home.html', {
        'plugin': plugin,
        'review': review,
    })



