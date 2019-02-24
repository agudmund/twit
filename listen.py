#!/usr/bin/env python
# *-* coding: utf-8 *-* 

import os
import sys
import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API



class StdOutListener(StreamListener):


    def on_data(self, data):

        result = json.loads(data)
        try:
            print (result['text'])
        except KeyError as e:
            return True

        return True

    def on_error(self, status):
        print (status)

if __name__ == '__main__':

    access_token = os.getenv("TWITTER_ACCESS_KEY")
    access_token_secret = os.getenv("TWITTER_SECRET_KEY")
    consumer_key = os.getenv("TWITTER_C_ACCESS_KEY")
    consumer_secret = os.getenv("TWITTER_C_SECRET_KEY")

    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret )
    stream = Stream(auth, l)

    data = stream.filter(track=[sys.argv[-1]])
