import tweepy

consumer_key = '3PKwir0C72itjwN47u9NJZ6q5'
consumer_secret = 'hog9QoFgtQi65QQrVvrlRlYnuqP5i9FjvkYElXfLfHnAd6kRs2'
access_token = '816511840243085312-t2ItiGmA5QYYsVoNm2Nz6Ym1iG1QExr'
access_token_secret = 'Qzi6pZOwavDsyiVvxCIXqbqbp7wd4gDdducbL9ylPUnCz'



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

places = api.geo_search(query='INDIA',granularity="country")

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status.text)


myStreamListener = MyStreamListener()
myStream = tweepy.Stream(api.auth, listener=myStreamListener)
myStream.filter(track=['Hello'],locations=[[[67.997691, 6.622513], [67.997691, 33.254896], [97.170672, 33.254896], [97.170672, 6.622513], [67.997691, 6.622513]]])

