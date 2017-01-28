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
user = api.get_user('creativedecodev')

def printings():
	public_tweets = api.home_timeline()

	for tweet in public_tweets:
		print tweet.text

	return True

def friends():
	print 'User: %s' % user
	print 'Screen Name: %s' % user.screen_name
	print 'Followers : %s' % user.followers_count
	print 'Friend List : '
	for friend in user.friends():
		print '\t%s' % friend.screen_name

if __name__ == '__main__':
	friends()