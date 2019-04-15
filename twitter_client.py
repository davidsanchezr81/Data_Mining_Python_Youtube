import os
import sys
from tweepy import API
from tweepy import OAuthHandler

def get_twitter_auth(): 
	''' Setting up Twitter Authentication
		Return tweety.OuthHandler Object '''
	try:
		# consumer_key = os.environ['TWITTER_CONSUMER_KEY']
		# consumer_secret = os.environ['TWITTER_CONSUMER_SECRET']
		# access_token = os.environ['TWITTER_ACCESS_TOKEN']
		# access_secret = os.environ['TWITTER_ACCESS_SECRET']

		consumer_key = ''
		consumer_secret = ''
		access_token = ''
		access_secret = ''
	except KeyError:
		sys.stderr.write("TWITTER_* environment variables not set\n")
		sys.exit(1)

	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_secret)

	return auth

def get_twitter_client():
	'''Setup Twitter API client
	Return tweepy.API object '''

	auth = get_twitter_auth()
	client = API(auth)
	return client