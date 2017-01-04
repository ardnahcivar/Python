import tweepy

consumer_key = '3PKwir0C72itjwN47u9NJZ6q5'
consumer_secret = 'hog9QoFgtQi65QQrVvrlRlYnuqP5i9FjvkYElXfLfHnAd6kRs2'
access_token = '816511840243085312-t2ItiGmA5QYYsVoNm2Nz6Ym1iG1QExr'
access_token_secret = 'Qzi6pZOwavDsyiVvxCIXqbqbp7wd4gDdducbL9ylPUnCz'



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


'''
places  = api.geo_search(query='INDIA',granularity="country")
place_id = places[0].id

tweets = api.search(q="place:%s" % place_id)
'''
#places = api.geo_search(query='INDIA',granularity="country")

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
            print('Name of place is'+str(status.place))
            print('User name is ->'+status.user.screen_name+' Tweet is ->'+status.text)



def filtering(myStream):
    def country():
        stream = myStream.filter(locations=[68.109700, 6.462700, 97.395359, 35.508701])
        return stream
    country()


myStreamListener = MyStreamListener()
myStream = tweepy.Stream(api.auth, listener=myStreamListener)
myStream = filtering(myStream)
myStream.filter(track=['hello'])
#myStream.filter(locations=[68.109700,6.462700,97.395359,35.508701] AND track=['hello'])
#locations=[-89.566389,42.998071,-89.246452,43.171916]
# india locations=[39.19922, 46.86019, 126.38672, -8.32021]
