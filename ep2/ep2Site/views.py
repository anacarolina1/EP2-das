from django.shortcuts import render
from forms import ReviewForm
import twitter
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from your.utils.lib import get_tweets


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


def get_tweets():
    """
    returns twitter feed with settings as described below, contains all related twitter settings
    """
    api = twitter.Api(consumer_key='yourcustomerkey',
                      consumer_secret='customerkeysecret',
                      access_token_key='accesstokenkey',
                      access_token_secret='accesstokensecret')

    context['tweets'] = get_tweets()

    return api.GetUserTimeline(screen_name='twitter_screen_name', exclude_replies=True, include_rts=False)  # includes entities
 