import tweepy
import re
import tweepy

consumer_key = '3PKwir0C72itjwN47u9NJZ6q5'
consumer_secret = 'hog9QoFgtQi65QQrVvrlRlYnuqP5i9FjvkYElXfLfHnAd6kRs2'
access_token = '816511840243085312-t2ItiGmA5QYYsVoNm2Nz6Ym1iG1QExr'
access_token_secret = 'Qzi6pZOwavDsyiVvxCIXqbqbp7wd4gDdducbL9ylPUnCz'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
user = input('enter the name of user u want to find')

image_url = api.get_user(user).profile_image_url_https
print('name is',api.get_user(user).name)
print(image_url)
correct_one = re.sub('_normal','_bigger',image_url)
print(correct_one)

