#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import twitter

def get_tweets():
    """
    returns twitter feed with settings as described below, contains all related twitter settings
    """

    api = twitter.Api(consumer_key='mWtgo7bALQUvgYgePj2l4eIpC',
                    consumer_secret='Xpd5q3FmY55JMOaoupJplbWZ2oGitRCiMxS3TP7sJywx00VyUt',
                    access_token_key='752670358088454144-InREWcI6y4eEgNcrkHV4YOQWM5fKNsF',
                    access_token_secret='r4DZgp3yqPvS285Jpn94YpTJyW9ejZB6j92jhNf5Q9kx8')

    return api.GetUserTimeline(screen_name='twitter_screen_name', exclude_replies=True, include_rts=False)  # includes entities

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])