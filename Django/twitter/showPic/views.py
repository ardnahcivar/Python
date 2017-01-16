import re
import tweepy
import json
from django.shortcuts import render
from django.http import HttpResponse
from showPic.forms import getUser
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


@csrf_exempt
def index(request):
    #return render(request, 'showPic/index.html')
    return render(request, 'showPic/matcher.html')



@csrf_exempt
def getUserData(request):
    if request.method == 'POST':
        print('GEEEEEEEEEEEEEEEEEEEEEEEEEEE')
        if 'name' in request.POST:
            try:
                #print(request.POST['names'])
                name = request.POST['name']
                consumer_key = '3PKwir0C72itjwN47u9NJZ6q5'
                consumer_secret = 'hog9QoFgtQi65QQrVvrlRlYnuqP5i9FjvkYElXfLfHnAd6kRs2'
                access_token = '816511840243085312-t2ItiGmA5QYYsVoNm2Nz6Ym1iG1QExr'
                access_token_secret = 'Qzi6pZOwavDsyiVvxCIXqbqbp7wd4gDdducbL9ylPUnCz'

                auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
                auth.set_access_token(access_token, access_token_secret)
                api = tweepy.API(auth)
                user_description = api.get_user(name).description

                image_url = api.get_user(name).profile_image_url_https
                correct_one = re.sub('_normal', '_bigger', image_url)
                data = {'image_url': correct_one, 'description': user_description}
                return HttpResponse(json.dumps(data))

            except Exception as e:
                    return HttpResponse(12)
    else:
        return HttpResponse('FAILURE')
