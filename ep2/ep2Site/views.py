from django.shortcuts import render
from forms import ReviewForm
import twitter
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView
from models import Review

class Home(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        return render(request, 'ep2Site/home.html')

    def get_tweets():
        """
        returns twitter feed with settings as described below, contains all related twitter settings
        """

        api = twitter.Api(consumer_key='mWtgo7bALQUvgYgePj2l4eIpC',
                        consumer_secret='Xpd5q3FmY55JMOaoupJplbWZ2oGitRCiMxS3TP7sJywx00VyUt',
                        access_token_key='752670358088454144-InREWcI6y4eEgNcrkHV4YOQWM5fKNsF',
                        access_token_secret='r4DZgp3yqPvS285Jpn94YpTJyW9ejZB6j92jhNf5Q9kx8')

        return api.GetUserTimeline(screen_name='twitter_screen_name', exclude_replies=True, include_rts=False)  # includes entities


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


class List(ListView):
    template_name = 'home.html'
    model = Review
    context_object = 'name'




#context['tweets'] = get_tweets()