import tweepy
import json
import matplotlib.pyplot as plot
from mpl_toolkits.basemap import Basemap

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
            #print(status)
            myData = {}
            myData['handle'] = str(status.user.screen_name)
            myData['tweet'] = str(status.text)
            myData['place'] = str(status.place)
            tdd = json.dumps(myData)
            #print(tdd)


            with open('twitter_data.json', 'w') as data:
                data.write(json.dump(tdd, data, indent=4, sort_keys=True,ensure_ascii=False))

            #print('Name of place is '+str(status.place))
            #print('User name is '+status.user.screen_name+' Tweet is '+status.text)


def filtering(myStream):
    def country():
        stream = myStream.filter(locations=[68.109700, 6.462700, 97.395359, 35.508701],track=['Hello'])
        return stream
    country()

"""
def filtering(myStream):
    stream = myStream.filter(locations=[68.109700, 6.462700, 97.395359, 35.508701], track=['Manish'])
    return stream
"""



if __name__=='__main__':
    fig  = plot.figure(figsize=(18,4), dpi=250)
    consumer_key = '3PKwir0C72itjwN47u9NJZ6q5'
    consumer_secret = 'hog9QoFgtQi65QQrVvrlRlYnuqP5i9FjvkYElXfLfHnAd6kRs2'
    access_token = '816511840243085312-t2ItiGmA5QYYsVoNm2Nz6Ym1iG1QExr'
    access_token_secret = 'Qzi6pZOwavDsyiVvxCIXqbqbp7wd4gDdducbL9ylPUnCz'

    plot.title("Tweet's around the world")

    # Declare map projection, size and resolution
    map = Basemap(projection='merc',
                  llcrnrlat=-80,
                  urcrnrlat=80,
                  llcrnrlon=-180,
                  urcrnrlon=180,
                  lat_ts=20,
                  resolution='l')

    map.bluemarble(scale=0.3)

    # Set interactive mode ON
    plot.ion()

    # Display map
    plot.show()

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(api.auth, listener=myStreamListener)
    myStream = filtering(myStream)



#print('filtering again')
#myStream.filter(track=['hello'])
#myStream.filter(locations=[68.109700,6.462700,97.395359,35.508701] AND track=['hello'])
#locations=[-89.566389,42.998071,-89.246452,43.171916]
# india locations=[39.19922, 46.86019, 126.38672, -8.32021]

