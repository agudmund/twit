#!/usr/bin/env python
# *-* coding: utf-8 *-* 

import os
import sys
import pip
import json
from time import sleep
import random
import pymongo
import argparse
import wikipedia

try:
    from tweepy.streaming import StreamListener
    from tweepy import OAuthHandler
    from tweepy import Stream
    from tweepy import API
except ImportError as e:
    print ("--[ Tweepy not installed, collecting it through pip.")
    pip.main(['install','tweepy'])

# Variables that contains the user credentials to access Twitter API
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
            print(textings)
        except KeyError as e:
            return True

        if args.stream:
            phrase = self.pick_word(textings)
            print(phrase)
            if args.wiki:
                try:
                    choices = wikipedia.search(self.pick_word(textings))
                    rez = wikipedia.summary(random.choice(choices))
                    print (rez,'\n\n\n\n')
                except:
                    rex = phrase
            else:
                rex = phrase
        else:
            rex = textings

        sleep(3)
        return True


    def scramblings(self):
        # Word scramble, the act of echoing sentences to find new creative ways of wording things.

        scramble = Jumble( rex )

        x= random.choice(scramble.sentence)
        y= random.choice(scramble.sentence)

        while x==y:
            y= random.choice(scramble.sentence)     

        if args.echo:
            api.update_status(' '.join(scramble.swap(x,y)))

            print (rex)

    def on_error(self, status):
        print (status)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Twitter event listener')
    parser.add_argument('-k','--key', type=str,help='Search string',action="store",required=True)
    parser.add_argument('-s','--stream', help='Prints out a word stream instead of the actual tweets',action="store_true")
    parser.add_argument('-w','--wiki', help='Retrieves a summary from wikipedia on the word chosen in the stream',action="store_true")
    parser.add_argument('-m','--mongo', help='Stores the results in a mongod database',action="store_true")
    parser.add_argument('-e','--echo', help='Echos random tweets to the feed, randomizing the word order',action="store_true")

    args = parser.parse_args()

    if args.wiki and not args.stream:
        print ('The --wiki flag requires the --stream flag')
        sys.exit(1)

    keyword = args.key

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret )
    stream = Stream(auth, l)
    api = API(auth)
    # print(api.home_timeline())
    try:
        data = stream.filter(track=expand_search(keyword))
    except UnicodeEncodeError as e:
        print ('This')
