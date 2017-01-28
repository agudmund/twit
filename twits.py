#!/usr/bin/env python

import os
import tweepy
from tweepy import OAuthHandler

access_token = os.getenv("TWITTER_ACCESS_KEY")
access_token_secret = os.getenv("TWITTER_SECRET_KEY")
consumer_key = os.getenv("TWITTER_C_ACCESS_KEY")
consumer_secret = os.getenv("TWITTER_C_SECRET_KEY")

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret )

api = tweepy.API(auth)
public_tweets = api.home_timeline()

for tweet in public_tweets:
	print tweet.text