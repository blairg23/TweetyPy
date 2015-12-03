import oauth2

def oauth_req(url, consumer_key, consumer_secret, key, secret, http_method="GET", post_body="", http_headers=None):
    consumer = oauth2.Consumer(key=consumer_key, secret=consumer_secret)
    token = oauth2.Token(key=key, secret=secret)
    client = oauth2.Client(consumer, token)
    resp, content = client.request( url, method=http_method, body=post_body, headers=http_headers )
    return content
 
# Consumer stuff:
consumer_key = '1snYlkdkoFZpv1JZ1Wo1CMj9G' # API Key
consumer_secret = 'lzQt07a5dVP5nVHmPWkxIWB40LNVuYlAEpRBvLmNNodZhCto5d' # API Secret
token = '1585229419-pDkXs7LsWzN6T68cJivEsGt65ycLu2xsttw9SCF'
token_secret = 'anjt0Itm15VOsHq1OL7EGhefClocMj07ZjdpyIKQ97dAA'
url = 'https://api.twitter.com/1.1/statuses/home_timeline.json'
home_timeline = oauth_req(url=url, consumer_key=consumer_key, consumer_secret=consumer_secret, key=token, secret=token_secret)
print home_timeline