#!/usr/bin/env python

import os
import tweepy
from tweepy import OAuthHandler

class Twitterings:
	def __init__(self):
		self.name = 'Twitterings'
		self.getenv()
		self.auth = OAuthHandler(self.consumer_key, self.consumer_secret)
		self.auth.set_access_token(self.access_token, self.access_token_secret )
		self.api = tweepy.API(self.auth)
		self.me = self.api.me()

	def speak(self,text):

		self.api.update_status(text)

		return True

	def get_user(self,name):
		user = self.api.get_user(name)
		print 'User: %s' % user.screen_name
		print '\tDescription: %s' % user.description
		print '\tLocation: %s' % user.location
		print '\tFollowers: %s' % user.followers_count
		print '\tFriends: %s' % user.friends_count

		return True

	def public(self):
		public_tweets = api.home_timeline()

		for tweet in public_tweets:
			print tweet.text

		return True

	def getenv(self, env=True,keyfile=None):
		if env==True:
			self.access_token = os.getenv("TWITTER_ACCESS_KEY")
			self.access_token_secret = os.getenv("TWITTER_SECRET_KEY")
			self.consumer_key = os.getenv("TWITTER_C_ACCESS_KEY")
			self.consumer_secret = os.getenv("TWITTER_C_SECRET_KEY")
		else:
			with open(keyfile) as data:
				result = data.readlines()

			for n in result.split('\n'):
				eval('self.%s'%n)


if __name__ == '__main__':
	twit = Twitterings()
	twit.get_user('creativedecodev')
