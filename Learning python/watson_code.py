import sys
import requests
import json
import operator
import tweepy
from watson_developer_cloud import PersonalityInsightsV2 as PersonalityInsights

#This function is used to receive and analyze
#the last 200 tweets of a Twitter handle using
#the Watson PI API
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
	    if (s.lang =='en'):
    			text += s.text.encode('utf-8')

	#Analyzing the 200 tweets with the Watson PI API
    pi_username = '981120c1-1b5a-4a92-89f0-79a7a7380d34'
    pi_password = 'EqrgW03ix1nP'
    pi_result = PersonalityInsights(username=pi_username, password=pi_password).profile(text)

	#Returning the Watson PI API results
    return pi_result

#This function is used to flatten the result
#from the Watson PI API
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


#This function is used to compare the results from
#the Watson PI API
def compare(dict1, dict2):
    compared_data = {}
    for keys in dict1:
        if dict1[keys] != dict2[keys]:
            compared_data[keys] = abs(dict1[keys] - dict2[keys])
    return compared_data

ardnahcivar
#The two Twitter handles
user_handle = "@Codecademy"
celebrity_handle = "@IBM"

#Analyze the user's tweets using the Watson PI API
user_result = analyze(user_handle)
celebrity_result = analyze(celebrity_handle)

#Flatten the results received from the Watson PI API
user = flatten(user_result)
celebrity = flatten(celebrity_result)

#Compare the results of the Watson PI API by calculating
#the distance between traits
compared_results = compare(user,celebrity)

#Sort the results
sorted_results = sorted(compared_results.items(), key=operator.itemgetter(1))

#Print the results to the user
for keys, value in sorted_results[:5]:
	print (keys)
	print (user[keys]),
	print ('->'),
	print (celebrity[keys]),
	print ('->'),
	print (compared_results[keys])
