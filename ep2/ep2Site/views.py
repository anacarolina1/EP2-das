from django.shortcuts import render
from forms import ReviewForm
import twitter
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.views.generic import View
from models import Review


def home(request):
	form = ReviewForm
	return render(request, 'ep2Site/home.html', {'form': form})




def index(request):

    if request.method == 'POST':
        form = MusicaForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            return present_output(form)
    else:
        form = MusicaForm()

    return render_to_response('output.html',
            {'form': form}, context_instance=RequestContext(request))

'''
def present_output(form):

    return HttpResponse([


        ])

'''

def music(request):
	form = ReviewForm
	return render(request, 'ep2Site/music.html', {'form': form})
