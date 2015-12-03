import certifi # SSL Certificates
import oauth2 as oauth 
import urlparse
import webbrowser

from requests_oauthlib import OAuth1
import json, requests


debug = True

# Consumer stuff:
consumer_key = '1snYlkdkoFZpv1JZ1Wo1CMj9G' # API Key
consumer_secret = 'lzQt07a5dVP5nVHmPWkxIWB40LNVuYlAEpRBvLmNNodZhCto5d' # API Secret

# Token stuff:
key =  '1585229419-pDkXs7LsWzN6T68cJivEsGt65ycLu2xsttw9SCF' # Token
secret = 'anjt0Itm15VOsHq1OL7EGhefClocMj07ZjdpyIKQ97dAA' # Token Secret

# OAuth URLs
request_token_url = 'https://api.twitter.com/oauth/request_token'
access_token_url = 'https://api.twitter.com/oauth/access_token'
authorize_url = 'https://api.twitter.com/oauth/authorize'

# Set up unauthorized client:
consumer = oauth.Consumer(consumer_key, consumer_secret)
client = oauth.Client(consumer)

# Get SSL Certificate:
client.ca_certs = certifi.where()

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

#print "Go to the following link in your browser:\n{redirect_link}".format(redirect_link=authorize_url+"?oauth_token="+request_token['oauth_token'])
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
token = oauth.Token(request_token['oauth_token'],
    request_token['oauth_token_secret'])
token.set_verifier(oauth_verifier)

# Set up authorized client:
client = oauth.Client(consumer, token)

# Get SSL Certificate:
client.ca_certs = certifi.where() 

resp, content = client.request(access_token_url, "POST")
access_token = dict(urlparse.parse_qsl(content))

if debug:
	print "Access Token:\n\t - oauth_token \t\t\t = {token} \n\t - oauth_token_secret \t = {token_secret}".format(
																												token=access_token['oauth_token'], 
																												token_secret=access_token['oauth_token_secret']
																												)

token = access_token['oauth_token']
token_secret = access_token['oauth_token']

# Authentication:
authenticated = False
try:
	_auth = OAuth1(consumer_key, consumer_secret, token, token_secret)			
	authenticated = True
	print _auth
except Exception, e:
	print '[ERROR]', e
	authenticated = False

if authenticated:
	url = 'https://api.twitter.com/1.1/'
	followers_url = 'followers/ids.json'
	friends_url = 'friends/ids.json'
	followers_response = requests.get(url=url+followers_url, auth=_auth)

	if followers_response.status_code == 200:
		print followers_response.json()
	else:
		print followers_response.url
