import tweepy

import tweepy

consumer_key = '3PKwir0C72itjwN47u9NJZ6q5'
consumer_secret = 'hog9QoFgtQi65QQrVvrlRlYnuqP5i9FjvkYElXfLfHnAd6kRs2'
access_token = '816511840243085312-t2ItiGmA5QYYsVoNm2Nz6Ym1iG1QExr'
access_token_secret = 'Qzi6pZOwavDsyiVvxCIXqbqbp7wd4gDdducbL9ylPUnCz'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
print(api.me())
places = api.geo_search(query="INDIA", granularity="country")
print('places are')
print(places)

place_id = places[0].id

tweets = api.search(q="place:%s" % place_id)

for tweet in tweets:
    print(tweet.text + " | " + tweet.place.name) if tweet.place else "Undefined place"

"""
public_tweets = api.home_timeline()
t = api.get_user('@PiyushMulik')
print(t)


print('Trending topics are')
trending = api.trends_available()
print(trending)
"""
