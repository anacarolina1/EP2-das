from django.shortcuts import render
from forms import ReviewForm
import twitter
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.views.generic import View
from models import Review


def home(request):

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.save()           
    else:
        form = ReviewForm()

    return render_to_response('ep2Site/home.html',
            {'form': form}, context_instance=RequestContext(request))





def music(request):
    form = ReviewForm
    return render(request, 'ep2Site/music.html', {'form': form})
