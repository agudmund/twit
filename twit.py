#!/usr/bin/env python

import os
import sys
import pip
import json
import random
import argparse
import wikipedia

try:
    from tweepy.streaming import StreamListener
    from tweepy import OAuthHandler
    from tweepy import Stream
except ImportError as e:
    print >> sys.stderr, "--[ Tweepy not installed, collecting it through pip."
    pip.main(['install','tweepy'])

parser = argparse.ArgumentParser(description='Twitter event listener')
parser.add_argument('-k','--key', type=str,help='Search string',action="store",required=True)
parser.add_argument('-s','--stream', type=str,help='Prints out a word stream instead of the actual tweets',action="store_true")
args = parser.parse_args()
keyword = args.key

#Variables that contains the user credentials to access Twitter API
access_token = os.getenv("TWITTER_ACCESS_KEY")
access_token_secret = os.getenv("TWITTER_SECRET_KEY")
consumer_key = os.getenv("TWITTER_C_ACCESS_KEY")
consumer_secret = os.getenv("TWITTER_C_SECRET_KEY")

def expand_search(token):
    '''Expands a keyword into upper,lower, and capitalized spelling.'''

    tokens = []
    tokens.append(keyword)                      #Normal
    tokens.append(r'%ss'%keyword)               #Plural
    tokens.append(keyword.capitalize())         #Capital case
    tokens.append(r'%ss'%keyword.capitalize())  #Capital case plural
    tokens.append(keyword.lower())              #Lower case
    tokens.append(r'%ss'%keyword.lower())       #Lower case plural
    tokens.append(keyword.upper())              #Upper case
    tokens.append(r'%ss'%keyword.upper())       #Upper case plural

    return tokens

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def pick_word(self,text):

        sampl = text.split()
        result = '%s%s%s' % ('\t'*random.randint(1,9),random.choice(sampl),'\n'*random.randint(1,3)) 

        return result

    def on_data(self, data):

        result = json.loads(data)
        try:
            textings = result['text']
        except KeyError as e:
            return True

        if args.stream:
            phrase = self.pick_word(textings)
            try:
                choices = wikipedia.search(self.pick_word(textings))
                print wikipedia.summary(random.choice(choices))
            except:
                print phrase
        else:
            print textings

        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret )
    stream = Stream(auth, l)

    data = stream.filter(track=expand_search(keyword))
