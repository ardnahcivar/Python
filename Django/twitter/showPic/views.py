import re
import tweepy
import json
import sys
import requests
import operator
from django.shortcuts import render
from django.http import HttpResponse
from showPic.forms import getUser
from django.views.decorators.csrf import csrf_exempt
from watson_developer_cloud import PersonalityInsightsV2 as PersonalityInsights


# Create your views here.


@csrf_exempt
def index(request):
    #return render(request, 'showPic/index.html')
    return render(request, 'showPic/matcher.html')



@csrf_exempt
def getUserData(request):
    if request.method == 'POST':
        print('GEEEEEEEEEEEEEEEEEEEEEEEEEEET')
        if 'first_user' in request.POST and 'second_user' in request.POST:
            print('GEEEEEEEEEEEEEEEEEEEEEEEEEEET')
            try:
                #print(request.POST['names'])
                first_user = request.POST['first_user']
                second_user = request.POST['second_user']

                consumer_key = '3PKwir0C72itjwN47u9NJZ6q5'
                consumer_secret = 'hog9QoFgtQi65QQrVvrlRlYnuqP5i9FjvkYElXfLfHnAd6kRs2'
                access_token = '816511840243085312-t2ItiGmA5QYYsVoNm2Nz6Ym1iG1QExr'
                access_token_secret = 'Qzi6pZOwavDsyiVvxCIXqbqbp7wd4gDdducbL9ylPUnCz'

                auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
                auth.set_access_token(access_token, access_token_secret)
                api = tweepy.API(auth)

                first_user_description = api.get_user(first_user).description
                second_user_description = api.get_user(second_user).description

                first_user_image_url = api.get_user(first_user).profile_image_url_https
                second_user_image_url = api.get_user(second_user).profile_image_url_https

                first_user_correct_one = re.sub('_normal', '_bigger', first_user_image_url)
                second_user_correct_one = re.sub('_normal', '_bigger', second_user_image_url)

                data = {'first_user': first_user, 'first_user_image_url': first_user_correct_one, 'first_user_description': first_user_description,
                        'second_user': second_user, 'second_user_image_url': second_user_correct_one, 'second_user_description': second_user_description}

                print('OOOOOOOOOOOOOOOOOOOOOO')
                return HttpResponse(json.dumps(data))

            except Exception as e:
                    return HttpResponse(12)
    else:
        return HttpResponse('FAILURE')


@csrf_exempt
def getInsights(request):
    if request.method == 'POST':
        print('in insights')
        if 'first_user' in request.POST and 'second_user' in request.POST:
            first_user = request.POST['first_user']
            second_user = request.POST['second_user']

            def analyze(handle):
                consumer_key = '3PKwir0C72itjwN47u9NJZ6q5'
                consumer_secret = 'hog9QoFgtQi65QQrVvrlRlYnuqP5i9FjvkYElXfLfHnAd6kRs2'
                access_token = '816511840243085312-t2ItiGmA5QYYsVoNm2Nz6Ym1iG1QExr'
                access_token_secret = 'Qzi6pZOwavDsyiVvxCIXqbqbp7wd4gDdducbL9ylPUnCz'

                auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
                auth.set_access_token(access_token, access_token_secret)
                api = tweepy.API(auth)

                statuses = api.user_timeline(screen_name=handle, count=200, include_rts=False)
                text = b''
                for s in statuses:
                    if (s.lang == 'en'):
                        text += s.text.encode('utf-8')

                # Analyzing the 200 tweets with the Watson PI API
                pi_username = '981120c1-1b5a-4a92-89f0-79a7a7380d34'
                pi_password = 'EqrgW03ix1nP'
                pi_result = PersonalityInsights(username=pi_username, password=pi_password).profile(text)

                # Returning the Watson PI API results
                return pi_result

            def flatten(orig):
                data = {}
                for c in orig['tree']['children']:
                    if 'children' in c:
                        for c2 in c['children']:
                            if 'children' in c2:
                                for c3 in c2['children']:
                                    if 'children' in c3:
                                        for c4 in c3['children']:
                                            if (c4['category'] == 'personality'):
                                                data[c4['id']] = c4['percentage']
                                                if 'children' not in c3:
                                                    if (c3['category'] == 'personality'):
                                                        data[c3['id']] = c3['percentage']
                return data

            def compare(dict1, dict2):
                compared_data = {}
                for keys in dict1:
                    if dict1[keys] != dict2[keys]:
                        compared_data[keys] = abs(dict1[keys] - dict2[keys])
                return compared_data

            user_handle = first_user
            celebrity_handle = second_user

            # Analyze the user's tweets using the Watson PI API
            user_result = analyze(user_handle)
            celebrity_result = analyze(celebrity_handle)

            # Flatten the results received from the Watson PI API
            user = flatten(user_result)
            celebrity = flatten(celebrity_result)

            # Compare the results of the Watson PI API by calculating
            # the distance between traits
            compared_results = compare(user, celebrity)

            # Sort the results
            sorted_results = sorted(compared_results.items(), key=operator.itemgetter(1))

            data = [{}]

            for keys, value in sorted_results[:5]:
                data.append({keys: {'user': user[keys], 'celebrity': celebrity[keys], 'comparison': compared_results[keys]}})

            print(data)
            return HttpResponse(json.dumps(data))

    else:
            return HttpResponse('FAILURE')


