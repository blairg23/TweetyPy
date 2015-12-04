# coding: utf-8
import oauth2
import urlparse
import webbrowser
import json
import requests
import os

from requests_oauthlib import OAuth1

class Tweety():
	def __init__(self, url='https://api.twitter.com/1.1/', consumer_key=None, consumer_secret=None, token=None, token_secret=None):
		self._consumer_key = consumer_key
		self._consumer_secret = consumer_secret
		self.url = url

		self.authenticated = False
		self.auth = None

		if not self.authenticated:
			try:
				self.auth = self.authenticate(consumer_key=self._consumer_key, consumer_secret=self._consumer_secret)	
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
			self._key = auth['_key']
			self._secret = auth['_secret']
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
			token = oauth2.Token(request_token['oauth_token'], request_token['oauth_token_secret'])
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
			self._key = access_token['oauth_token']
			self._secret = access_token['oauth_token_secret']			

			# Save the file (totally insecure)
			token_dict = {'_key': self._key, '_secret': self._secret}
			with open('oauth.json', 'w') as outfile:
				json.dump(token_dict, outfile)


	def twitter_request(self, url, http_method='GET', payload={}, http_headers=None): #key, secret, http_method="GET", post_body="", http_headers=None):
		'''
		Performs an authenticated request to the given url 
		using the given consumer key and secret, http method, body (if POST), 
		and headers.
		'''						
		#client = oauth2.Client(self.auth['consumer'], self.auth['token'])
		self._auth = OAuth1(self._consumer_key, self._consumer_secret, self._key, self._secret)
		#resp, content = client.request(url, method=http_method, body=post_body, headers=http_headers)

		response = requests.request(method=http_method, url=url, auth=self._auth, params=payload)		
		#return content
		return response.content

	def get_credentials(self):
		'''
		Get current user's Twitter credentials.

		Get Credentials: https://dev.twitter.com/rest/reference/get/account/verify_credentials
		'''
		creds_url = 'account/verify_credentials.json'
		credentials = self.twitter_request(url=self.url+creds_url)
		#print 'Credentials: ', credentials
		return credentials

	def remove_non_friends(self):
		'''
		Removes any "followed" Twitter users who are not "friends".

		Get Friends: https://dev.twitter.com/rest/reference/get/friends/ids
		Get Followers: https://dev.twitter.com/rest/reference/get/followers/ids
		Get Friendships: https://dev.twitter.com/rest/reference/get/friendships/lookup
		Destroy Friendships: https://dev.twitter.com/rest/reference/post/friendships/destroy

		'''
		followers_url = 'followers/ids.json'
		friends_url = 'friends/ids.json'
		friendships_url = 'friendships/lookup.json'
		destroy_friend_url = 'friendships/destroy.json'

		followers = json.loads(self.twitter_request(url=self.url+followers_url))
		print 'Followers: ', followers
		friends = json.loads(self.twitter_request(url=self.url+friends_url))
		print 'Friends: ', friends
		credentials = json.loads(self.get_credentials())
		screen_name = credentials['screen_name']
		print 'Screen Name:', screen_name

		num_followed = 0
		for friend_id in friends['ids']:
			if friend_id not in followers['ids']:				
				payload = {
					'user_id': friend_id
				}
				destroy = json.loads(self.twitter_request(http_method='POST', url=self.url+destroy_friend_url, payload=payload))
				print 'Stopped following {screen_name}, user_id={user_id}'.format(screen_name=destroy['screen_name'], user_id=friend_id)
				num_followed += 1
		print 'Removed {num_followed} friends.'.format(num_followed=num_followed)
		

if __name__ == '__main__':
	# Consumer stuff:
	consumer_key = 'RcPVxXd9RqG0lc6ITkZFcImXh' # API Key
	consumer_secret = 'vE95Ub92p621MyyEmJ5ulmXLIi0rRuFi1Z1ux6af51xRUhSvK0' # API Secret	
	twitter_client = Tweety(consumer_key=consumer_key, consumer_secret=consumer_secret)
	twitter_client.remove_non_friends()	



