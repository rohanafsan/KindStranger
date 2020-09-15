import twitter
import csv
import time
import json
from helpline import Helpline


# rateLimit = 180
# sleepTime = 3600/180


# Call to the twitter Api to get it initiated
apiCall = twitter.Api(consumer_key = '',
                      consumer_secret  = '',
                      access_token_key = '',
                      access_token_secret = '')



# Gets a specific users most recent tweets
def getUserTweets(userId):
    lot = []
    try:
        user = apiCall.GetUser(user_id=None, screen_name=userId, include_entities=True, return_json=False)
        tweetDump = apiCall.GetUserTimeline(user.id)
        print(tweetDump)
        for tweet in tweetDump:
            lot.extend({tweet.text})
        return lot
    except:
        print("Could not fetch tweets")
        return None

# Direct Messages a user with resources and helplines based on the users geolocation 
def dMUser(userId):
    country = ''
    user = apiCall.GetUser(user_id=None, screen_name=userId)
    country = str(user.status.place['country'])

    for k, v in Helpline.items():
        if country == k:
            message_text = 'KindStranger noticed that you were feeling down. Here are some free resources in your country you can reach out to if you wish to talk to someone:\n'
            dm = apiCall.PostDirectMessage(message_text, user_id=user.id, screen_name=None, return_json=True)
            message_text = 'Numbers:' + '\n'
            for numbers in Helpline[country]['Number']:
                message_text += numbers[0] + ": " + numbers[1] + '\n'
            dm = apiCall.PostDirectMessage(message_text, user_id=user.id, screen_name=None, return_json=True)
            for websites in Helpline[country]['Website']:
                message_text += websites[1] + '\n'
            dm = apiCall.PostDirectMessage(message_text, user_id=user.id, screen_name=None, return_json=True)
            return 0
        else:
            continue
    country = 'Worldwide'
    message_text = 'KindStranger noticed that you were feeling down. Here are some free resources you can reach out to if you wish to talk to someone:\n'
    dm = apiCall.PostDirectMessage(message_text, user_id=user.id, screen_name=None, return_json=True)
    message_text = 'Numbers:' + '\n'
    for websites in Helpline[country]['Website']:
        message_text += websites[1] + '\n'
    dm = apiCall.PostDirectMessage(message_text, user_id=user.id, screen_name=None, return_json=True)
    return 0
