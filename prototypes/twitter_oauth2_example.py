# coding: utf-8
import oauth2
import urlparse
import webbrowser
import json
import requests
import os

class TwitterClient():
	def __init__(self, url='https://api.twitter.com/1.1/', consumer_key=None, consumer_secret=None, token=None, token_secret=None):
		self.consumer_key = consumer_key
		self.consumer_secret = consumer_secret
		self.url = url

		self.authenticated = False
		self.auth = None


		# Don't need this line once we have the key and secret in hand:
		if not self.authenticated:
			try:
				self.auth = self.authenticate(consumer_key=consumer_key, consumer_secret=consumer_secret)	
				self.authenticated = True
				print 'yep'
			except Exception, e:
				print '[ERROR]', e
				self.authenticated = False
				print 'nope'

	def authenticate(self, consumer_key=None, consumer_secret=None, debug=False):
		'''
		Given a consumer key and secret, returns a dictionary with the
		consumer and token.
		'''
		# Set up unauthorized consumer:
		consumer = oauth2.Consumer(key=consumer_key, secret=consumer_secret)
		
		if os.path.exists('oauth.json'):	
			with open('oauth.json') as infile:
				auth = json.load(infile)
			token = oauth2.Token(key=auth['request_token'], secret=auth['request_token_secret'])			
		else:
			# OAuth URLs:
			request_token_url = 'https://api.twitter.com/oauth/request_token'
			access_token_url = 'https://api.twitter.com/oauth/access_token'
			authorize_url = 'https://api.twitter.com/oauth/authorize'
			
			# Set up unauthorized client:
			client = oauth2.Client(consumer)

			# Step 1: Get a request token. This is a temporary token that is used for
			# having the user authorize an access token and to sign the request to obtain
			# said access token.
			resp, content = client.request(request_token_url, "GET")
			if resp['status'] != '200':
				raise Exception("Invalid response %s." % resp['status'])    

			if debug:
				print "Response:\n{resp}\n".format(resp=resp) 
				print "Content:\n{content}\n".format(content=content)

			request_token = dict(urlparse.parse_qsl(content))

			if debug:
				print "Request Token:\n\t - oauth_token \t\t\t = {token} \n\t - oauth_token_secret \t = {token_secret}".format(
																															token=request_token['oauth_token'], 
																															token_secret=request_token['oauth_token_secret']
																															)	
			# Step 2: Redirect to the provider. Since this is a CLI script we do not
			# redirect. In a web application you would redirect the user to the URL 
			# below.

			# Open the web browser for the user to click accept and copy the pin:
			webbrowser.open(url=authorize_url+"?oauth_token="+request_token['oauth_token'])

			# After the user has granted access to you, the consumer, the provider will
			# redirect you to whatever URL you have told them to redirect to. You can 
			# usually define this in the oauth_callback argument as well.
			accepted = 'n'
			while accepted.lower() == 'n':
			    accepted = raw_input('Have you authorized me? (y/n) ')
			oauth_verifier = raw_input('What is the PIN? ')

			# Step 3: Once the consumer has redirected the user back to the oauth_callback
			# URL you can request the access token the user has approved. You use the 
			# request token to sign this request. After this is done you throw away the
			# request token and use the access token returned. You should store this 
			# access token somewhere safe, like a database, for future use.	
			token = oauth2.Token(request_token['oauth_token'],
			    request_token['oauth_token_secret'])
			token.set_verifier(oauth_verifier)

			# Set up authorized client:
			client = oauth2.Client(consumer, token)

			resp, content = client.request(access_token_url, "POST")
			access_token = dict(urlparse.parse_qsl(content))

			if debug:
				print "Access Token:\n\t - oauth_token \t\t\t = {token} \n\t - oauth_token_secret \t = {token_secret}".format(
																															token=access_token['oauth_token'], 
																															token_secret=access_token['oauth_token_secret']
																															)
			request_token = access_token['oauth_token']
			request_token_secret = access_token['oauth_token_secret']			

			# Save the file (totally insecure)
			token_dict = {'request_token': request_token, 'request_token_secret': request_token_secret}
			with open('oauth.json', 'w') as outfile:				
				json.dump(token_dict, outfile)

			token = oauth2.Token(key=request_token, secret=request_token_secret)
		return {'consumer': consumer, 'token': token}

	def twitter_request(self, url, http_method="GET", post_body="", http_headers=None): #key, secret, http_method="GET", post_body="", http_headers=None):
		'''
		Performs an authenticated request to the given url 
		using the given consumer key and secret, http method, body (if POST), 
		and headers.
		'''						
		client = oauth2.Client(self.auth['consumer'], self.auth['token'])
		resp, content = client.request(url, method=http_method, body=post_body, headers=http_headers)
		return content

	def get_credentials(self):
		'''
		Get current user's Twitter credentials.

		Get Credentials: https://dev.twitter.com/rest/reference/get/account/verify_credentials
		'''
		creds_url = 'account/verify_credentials.json'
		credentials = self.twitter_request(url=self.url+creds_url)
		print 'Credentials: ', credentials
		return credentials

	def remove_non_friends(self):
		'''
		Removes any "followed" Twitter users who are not "friends".

		Get Friends: https://dev.twitter.com/rest/reference/get/friends/ids
		Get Followers: https://dev.twitter.com/rest/reference/get/followers/ids
		Get Friendships: https://dev.twitter.com/rest/reference/get/friendships/lookup

		'''
		followers_url = 'followers/ids.json'
		friends_url = 'friends/ids.json'
		followers = self.twitter_request(url=self.url+followers_url)
		print 'Followers: ', followers
		friends = self.twitter_request(url=self.url+friends_url)
		print 'Friends: ', friends



if __name__ == '__main__':
	# Consumer stuff:
	consumer_key = '1snYlkdkoFZpv1JZ1Wo1CMj9G' # API Key
	consumer_secret = 'lzQt07a5dVP5nVHmPWkxIWB40LNVuYlAEpRBvLmNNodZhCto5d' # API Secret
	url = 'https://api.twitter.com/1.1/statuses/home_timeline.json'
	twitter_client = TwitterClient(consumer_key=consumer_key, consumer_secret=consumer_secret)
	twitter_client.remove_non_friends()
	twitter_client.get_credentials()
	# home_timeline = twitter_client.twitter_request(url=url, consumer_key=consumer_key, consumer_secret=consumer_secret)
	# print home_timeline



