#!/usr/bin/env python

import os
import sys
import json
import random

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = os.getenv("TWITTER_ACCESS_KEY")
access_token_secret = os.getenv("TWITTER_SECRET_KEY")
consumer_key = os.getenv("TWITTER_C_ACCESS_KEY")
consumer_secret = os.getenv("TWITTER_C_SECRET_KEY")

keyword = sys.argv[-1]

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def pick_word(self,text):

        sampl = text.split()
        result = '%s%s%s' % ('\t'*random.randint(1,9),random.choice(sampl),'\n'*random.randint(1,3)) 

        return result

    def on_data(self, data):

        textings = json.loads(data)['text']

        print self.pick_word(textings)

        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    data = stream.filter(track=['%ss'%keyword.capitalize(),keyword.capitalize(),'%ss'%keyword,keyword])
