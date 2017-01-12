import sys
import operator
import requests
import json
import twitter
from watson_developer_cloud import PersonalityInsightsV2 as PersonalityInsights



twitter_consumer_key = '3PKwir0C72itjwN47u9NJZ6q5'
twitter_consumer_secret = 'hog9QoFgtQi65QQrVvrlRlYnuqP5i9FjvkYElXfLfHnAd6kRs2'
twitter_access_token = '816511840243085312-t2ItiGmA5QYYsVoNm2Nz6Ym1iG1QExr'
twitter_access_token_secret = 'Qzi6pZOwavDsyiVvxCIXqbqbp7wd4gDdducbL9ylPUnCz'


def analyze(handle):
    twitter_consumer_key = ''


twitter_consumer_secret = ''
twitter_access_token = ''
twitter_access_secret = ''

twitter_api = twitter.Api(consumer_key=twitter_consumer_key, consumer_secret=twitter_consumer_secret,
                          access_token_key=twitter_access_token, access_token_secret=twitter_access_secret)

statuses = twitter_api.GetUserTimeline(screen_name=handle, count=200, include_rts=False)

text = ""

for status in statuses:
    if (status.lang == 'en'):
        text += status.text.encode('utf-8')

pi_username = '981120c1-1b5a-4a92-89f0-79a7a7380d34'
pi_password = 'EqrgW03ix1nP'

personality_insights = PersonalityInsights(username=pi_username, password=pi_password)
pi_result = personality_insights.profile(text)
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
    compare_data = {}
    for keys in dict1:
        if dict1[keys] != dict2[keys]:
            compared_data[keys] = abs(dict1[keys] = dict2[keys])
            return compared_data

    user_handle = "@Codecademy"
    celebrity_handle = "@IBM"

    user_result = analyze(user_handle)
    celebrity_result = analyze(celebrity_handle)

    user = flatten(user_result)
    celebrity = flatten(celebrity_result)

    compared_results = compare(user, celebrity)

    sorted_result = sorted(compared_results.items(), key=operator.itemgetter(1))

    for keys, value in sorted_result[:5]:
        print
        keys,
        print(user[keys]),
        print('->')
        print(celebrity[keys]),
        print('->')
        print(compared_results[keys])
