import re
import tweepy
from django.shortcuts import render
from django.http import HttpResponse
from showPic.forms import getUser
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


@csrf_exempt
def index(request):
    return render(request, 'showPic/index.html')



@csrf_exempt
def getUserData(request):
    if request.method == 'POST':
        if 'name' in request.POST:
            try:
                name = request.POST['name']
                consumer_key = '3PKwir0C72itjwN47u9NJZ6q5'
                consumer_secret = 'hog9QoFgtQi65QQrVvrlRlYnuqP5i9FjvkYElXfLfHnAd6kRs2'
                access_token = '816511840243085312-t2ItiGmA5QYYsVoNm2Nz6Ym1iG1QExr'
                access_token_secret = 'Qzi6pZOwavDsyiVvxCIXqbqbp7wd4gDdducbL9ylPUnCz'

                auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
                auth.set_access_token(access_token, access_token_secret)
                api = tweepy.API(auth)

                image_url = api.get_user(name).profile_image_url_https
                correct_one = re.sub('_normal', '_bigger', image_url)

                return HttpResponse(correct_one)

            except Exception as e:
                    return HttpResponse(12)

    else:
        return HttpResponse('FAILURE')
