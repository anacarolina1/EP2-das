from django.shortcuts import render
from forms import ReviewForm

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse


def music_list(request):
	form = ReviewForm
	return render(request, 'ep2Site/music_list.html', {'form': form})




def index(request):

    ''' Defines the actions we want to perform when invoking 
        the URL ( here http://127.0.0.1:8000/hw1/).'''

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
