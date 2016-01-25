# coding: utf-8
'''
Name: TwitterClient.py
Author: Blair Gemmer
Version: 20151204
Description: Implements the Twitter API interface.
'''
from BaseTwitterClient import BaseTwitterClient

import requests, logging, json
from requests_oauthlib import OAuth1

class TwitterClient(BaseTwitterClient):
	def __init__(self, url='https://api.twitter.com/1.1/', consumer_key=None, consumer_secret=None, key=None, secret=None, debug=False):
		# Credentials:
		self._consumer_key = consumer_key
		self._consumer_secret = consumer_secret
		self._key = key
		self._secret = secret

		# Twitter API's base URL:
		self._url = url

		# If we want debug information:
		self._debug = debug

		# Authenticate the user:
		self._authenticated = self.authenticate()


	def authenticate(self):
		'''
		Authenticate user.
		'''
		try:            
			self._auth = OAuth1(self._consumer_key, self._consumer_secret, self._key, self._secret)
		except Exception, e:
			logging.exception(e)
			return False
		return True

	def request(self, url=None, http_method='GET', payload={}, http_headers=None):
		if self._authenticated:
			print '[Authenticated]'
			response = requests.request(method=http_method, url=url, auth=self._auth, params=payload)
			if response.status_code == 200:
				return response.content
			else:
				print '[ERROR: ]', response.status_code
				return False				
		else:
			print '[Not Authenticated]'
	
	def get_statuses_mentions_timeline(self):
		'''
		Implements https://api.twitter.com/1.1//statuses/mentions_timeline.json
		Documentation URL: https://dev.twitter.com/rest/reference/get/statuses/mentions_timeline
		'''
		payload={
		}
		content = self.request(http_method='GET', payload=payload)
		return content

	def get_statuses_user_timeline(self):
		'''
		Implements https://api.twitter.com/1.1//statuses/user_timeline.json
		Documentation URL: https://dev.twitter.com/rest/reference/get/statuses/user_timeline
		'''
		payload={
		}
		content = self.request(http_method='GET', payload=payload)
		return content

	def get_statuses_home_timeline(self):
		'''
		Implements https://api.twitter.com/1.1//statuses/home_timeline.json
		Documentation URL: https://dev.twitter.com/rest/reference/get/statuses/home_timeline
		'''
		payload={
		}
		content = self.request(http_method='GET', payload=payload)
		return content

	def get_statuses_retweets_of_me(self):
		'''
		Implements https://api.twitter.com/1.1//statuses/retweets_of_me.json
		Documentation URL: https://dev.twitter.com/rest/reference/get/statuses/retweets_of_me
		'''
		payload={
		}
		content = self.request(http_method='GET', payload=payload)
		return content

	def get_statuses_retweets_id(self):
		'''
		Implements https://api.twitter.com/1.1//statuses/retweets/id.json
		Documentation URL: https://dev.twitter.com/rest/reference/get/statuses/retweets/id
		'''
		payload={
		}
		content = self.request(http_method='GET', payload=payload)
		return content

	def get_statuses_show_id(self):
		'''
		Implements https://api.twitter.com/1.1//statuses/show/id.json
		Documentation URL: https://dev.twitter.com/rest/reference/get/statuses/show/id
		'''
		payload={
		}
		content = self.request(http_method='GET', payload=payload)
		return content

	def post_statuses_destroy_id(self):
		'''
		Implements https://api.twitter.com/1.1//statuses/destroy/id.json
		Documentation URL: https://dev.twitter.com/rest/reference/post/statuses/destroy/id
		'''
		payload={
		}
		content = self.request(http_method='POST', payload=payload)
		return content

	def post_statuses_update(self):
		'''
		Implements https://api.twitter.com/1.1//statuses/update.json
		Documentation URL: https://dev.twitter.com/rest/reference/post/statuses/update
		'''
		payload={
		}
		content = self.request(http_method='POST', payload=payload)
		return content

	def post_statuses_retweet_id(self):
		'''
		Implements https://api.twitter.com/1.1//statuses/retweet/id.json
		Documentation URL: https://dev.twitter.com/rest/reference/post/statuses/retweet/id
		'''
		payload={
		}
		content = self.request(http_method='POST', payload=payload)
		return content

	def post_statuses_update_with_media(self):
		'''
		Implements https://api.twitter.com/1.1//statuses/update_with_media.json
		Documentation URL: https://dev.twitter.com/rest/reference/post/statuses/update_with_media
		'''
		payload={
		}
		content = self.request(http_method='POST', payload=payload)
		return content

	def get_statuses_oembed(self):
		'''
		Implements https://api.twitter.com/1.1//statuses/oembed.json
		Documentation URL: https://dev.twitter.com/rest/reference/get/statuses/oembed
		'''
		payload={
		}
		content = self.request(http_method='GET', payload=payload)
		return content

	def get_statuses_retweeters_ids(self):
		'''
		Implements https://api.twitter.com/1.1//statuses/retweeters/ids.json
		Documentation URL: https://dev.twitter.com/rest/reference/get/statuses/retweeters/ids
		'''
		payload={
		}
		content = self.request(http_method='GET', payload=payload)
		return content

	def get_statuses_lookup(self):
		'''
		Implements https://api.twitter.com/1.1//statuses/lookup.json
		Documentation URL: https://dev.twitter.com/rest/reference/get/statuses/lookup
		'''
		payload={
		}
		content = self.request(http_method='GET', payload=payload)
		return content

	def post_media_upload(self):
		'''
		Implements https://api.twitter.com/1.1//media/upload.json
		Documentation URL: https://dev.twitter.com/rest/reference/post/media/upload
		'''
		payload={
		}
		content = self.request(http_method='POST', payload=payload)
		return content

	def post_media_upload_chunked(self):
		'''
		Implements https://api.twitter.com/1.1//media/upload.json
		Documentation URL: https://dev.twitter.com/rest/reference/post/media/upload
		'''
		payload={
		}
		content = self.request(http_method='POST', payload=payload)
		return content

	def get_direct_messages_sent(self):
		'''
		Implements https://api.twitter.com/1.1//direct_messages/sent.json
		Documentation URL: https://dev.twitter.com/rest/reference/get/direct_messages/sent
		'''
		payload={
		}
		content = self.request(http_method='GET', payload=payload)
		return content

	def get_direct_messages_show(self):
		'''
		Implements https://api.twitter.com/1.1//direct_messages/show.json
		Documentation URL: https://dev.twitter.com/rest/reference/get/direct_messages/show
		'''
		payload={
		}
		content = self.request(http_method='GET', payload=payload)
		return content

	def get_search_tweets(self):
		'''
		Implements https://api.twitter.com/1.1//search/tweets.json
		Documentation URL: https://dev.twitter.com/rest/reference/get/search/tweets
		'''
		payload={
		}
		content = self.request(http_method='GET', payload=payload)
		return content

	def get_direct_messages(self):
		'''
		Implements https://api.twitter.com/1.1//direct_messages.json
		Documentation URL: https://dev.twitter.com/rest/reference/get/direct_messages
		'''
		payload={
		}
		content = self.request(http_method='GET', payload=payload)
		return content

	def post_direct_messages_destroy(self):
		'''
		Implements https://api.twitter.com/1.1//direct_messages/destroy.json
		Documentation URL: https://dev.twitter.com/rest/reference/post/direct_messages/destroy
		'''
		payload={
		}
		content = self.request(http_method='POST', payload=payload)
		return content

	def post_direct_messages_new(self):
		'''
		Implements https://api.twitter.com/1.1//direct_messages/new.json
		Documentation URL: https://dev.twitter.com/rest/reference/post/direct_messages/new
		'''
		payload={
		}
		content = self.request(http_method='POST', payload=payload)
		return content

	def get_friendships_no_retweets_ids(self):
		'''
		Implements https://api.twitter.com/1.1//friendships/no_retweets/ids.json
		Documentation URL: https://dev.twitter.com/rest/reference/get/friendships/no_retweets/ids
		'''
		payload={
		}
		content = self.request(http_method='GET', payload=payload)
		return content

	def get_friends_ids(self):
		'''
		Implements https://api.twitter.com/1.1//friends/ids.json
		Documentation URL: https://dev.twitter.com/rest/reference/get/friends/ids
		'''
		payload={
		}
		content = self.request(http_method='GET', payload=payload)
		return content

	def get_followers_ids(self):
		'''
		Implements https://api.twitter.com/1.1//followers/ids.json
		Documentation URL: https://dev.twitter.com/rest/reference/get/followers/ids
		'''
		payload={
		}
		content = self.request(http_method='GET', payload=payload)
		return content

	def get_friendships_incoming(self):
		'''
		Implements https://api.twitter.com/1.1//friendships/incoming.json
		Documentation URL: https://dev.twitter.com/rest/reference/get/friendships/incoming
		'''
		payload={
		}
		content = self.request(http_method='GET', payload=payload)
		return content

	def get_friendships_outgoing(self):
		'''
		Implements https://api.twitter.com/1.1//friendships/outgoing.json
		Documentation URL: https://dev.twitter.com/rest/reference/get/friendships/outgoing
		'''
		payload={
		}
		content = self.request(http_method='GET', payload=payload)
		return content

	def post_friendships_create(self):
		'''
		Implements https://api.twitter.com/1.1//friendships/create.json
		Documentation URL: https://dev.twitter.com/rest/reference/post/friendships/create
		'''
		payload={
		}
		content = self.request(http_method='POST', payload=payload)
		return content

	def post_friendships_destroy(self):
		'''
		Implements https://api.twitter.com/1.1//friendships/destroy.json
		Documentation URL: https://dev.twitter.com/rest/reference/post/friendships/destroy
		'''
		payload={
		}
		content = self.request(http_method='POST', payload=payload)
		return content

	def post_friendships_update(self):
		'''
		Implements https://api.twitter.com/1.1//friendships/update.json
		Documentation URL: https://dev.twitter.com/rest/reference/post/friendships/update
		'''
		payload={
		}
		content = self.request(http_method='POST', payload=payload)
		return content

	def get_friendships_show(self):
		'''
		Implements https://api.twitter.com/1.1//friendships/show.json
		Documentation URL: https://dev.twitter.com/rest/reference/get/friendships/show
		'''
		payload={
		}
		content = self.request(http_method='GET', payload=payload)
		return content

	def get_friends_list(self):
		'''
		Implements https://api.twitter.com/1.1//friends/list.json
		Documentation URL: https://dev.twitter.com/rest/reference/get/friends/list
		'''
		payload={
		}
		content = self.request(http_method='GET', payload=payload)
		return content

	def get_followers_list(self):
		'''
		Implements https://api.twitter.com/1.1//followers/list.json
		Documentation URL: https://dev.twitter.com/rest/reference/get/followers/list
		'''
		payload={
		}
		content = self.request(http_method='GET', payload=payload)
		return content

	def get_friendships_lookup(self):
		'''
		Implements https://api.twitter.com/1.1//friendships/lookup.json
		Documentation URL: https://dev.twitter.com/rest/reference/get/friendships/lookup
		'''
		payload={
		}
		content = self.request(http_method='GET', payload=payload)
		return content

	def get_account_settings(self):
		'''
		Implements https://api.twitter.com/1.1//account/settings.json
		Documentation URL: https://dev.twitter.com/rest/reference/get/account/settings
		'''
		payload={
		}
		content = self.request(http_method='GET', payload=payload)
		return content

	def get_account_verify_credentials(self):
		'''
		Implements https://api.twitter.com/1.1//account/verify_credentials.json
		Documentation URL: https://dev.twitter.com/rest/reference/get/account/verify_credentials
		'''
		payload={
		}
		content = self.request(http_method='GET', payload=payload)
		return content

	def post_account_settings(self):
		'''
		Implements https://api.twitter.com/1.1//account/settings.json
		Documentation URL: https://dev.twitter.com/rest/reference/post/account/settings
		'''
		payload={
		}
		content = self.request(http_method='POST', payload=payload)
		return content

	def post_account_update_delivery_device(self):
		'''
		Implements https://api.twitter.com/1.1//account/update_delivery_device.json
		Documentation URL: https://dev.twitter.com/rest/reference/post/account/update_delivery_device
		'''
		payload={
		}
		content = self.request(http_method='POST', payload=payload)
		return content

	def post_account_update_profile(self):
		'''
		Implements https://api.twitter.com/1.1//account/update_profile.json
		Documentation URL: https://dev.twitter.com/rest/reference/post/account/update_profile
		'''
		payload={
		}
		content = self.request(http_method='POST', payload=payload)
		return content

	def post_account_update_profile_background_image(self):
		'''
		Implements https://api.twitter.com/1.1//account/update_profile_background_image.json
		Documentation URL: https://dev.twitter.com/rest/reference/post/account/update_profile_background_image
		'''
		payload={
		}
		content = self.request(http_method='POST', payload=payload)
		return content

	def post_account_update_profile_image(self):
		'''
		Implements https://api.twitter.com/1.1//account/update_profile_image.json
		Documentation URL: https://dev.twitter.com/rest/reference/post/account/update_profile_image
		'''
		payload={
		}
		content = self.request(http_method='POST', payload=payload)
		return content

	def get_blocks_list(self):
		'''
		Implements https://api.twitter.com/1.1//blocks/list.json
		Documentation URL: https://dev.twitter.com/rest/reference/get/blocks/list
		'''
		payload={
		}
		content = self.request(http_method='GET', payload=payload)
		return content

	def get_blocks_ids(self):
		'''
		Implements https://api.twitter.com/1.1//blocks/ids.json
		Documentation URL: https://dev.twitter.com/rest/reference/get/blocks/ids
		'''
		payload={
		}
		content = self.request(http_method='GET', payload=payload)
		return content

	def post_blocks_create(self):
		'''
		Implements https://api.twitter.com/1.1//blocks/create.json
		Documentation URL: https://dev.twitter.com/rest/reference/post/blocks/create
		'''
		payload={
		}
		content = self.request(http_method='POST', payload=payload)
		return content

	def post_blocks_destroy(self):
		'''
		Implements https://api.twitter.com/1.1//blocks/destroy.json
		Documentation URL: https://dev.twitter.com/rest/reference/post/blocks/destroy
		'''
		payload={
		}
		content = self.request(http_method='POST', payload=payload)
		return content

	def get_users_lookup(self):
		'''
		Implements https://api.twitter.com/1.1//users/lookup.json
		Documentation URL: https://dev.twitter.com/rest/reference/get/users/lookup
		'''
		payload={
		}
		content = self.request(http_method='GET', payload=payload)
		return content

	def get_users_show(self):
		'''
		Implements https://api.twitter.com/1.1//users/show.json
		Documentation URL: https://dev.twitter.com/rest/reference/get/users/show
		'''
		payload={
		}
		content = self.request(http_method='GET', payload=payload)
		return content

	def get_users_search(self):
		'''
		Implements https://api.twitter.com/1.1//users/search.json
		Documentation URL: https://dev.twitter.com/rest/reference/get/users/search
		'''
		payload={
		}
		content = self.request(http_method='GET', payload=payload)
		return content

	def post_account_remove_profile_banner(self):
		'''
		Implements https://api.twitter.com/1.1//account/remove_profile_banner.json
		Documentation URL: https://dev.twitter.com/rest/reference/post/account/remove_profile_banner
		'''
		payload={
		}
		content = self.request(http_method='POST', payload=payload)
		return content

	def post_account_update_profile_banner(self):
		'''
		Implements https://api.twitter.com/1.1//account/update_profile_banner.json
		Documentation URL: https://dev.twitter.com/rest/reference/post/account/update_profile_banner
		'''
		payload={
		}
		content = self.request(http_method='POST', payload=payload)
		return content

	def get_users_profile_banner(self):
		'''
		Implements https://api.twitter.com/1.1//users/profile_banner.json
		Documentation URL: https://dev.twitter.com/rest/reference/get/users/profile_banner
		'''
		payload={
		}
		content = self.request(http_method='GET', payload=payload)
		return content

	def post_mutes_users_create(self):
		'''
		Implements https://api.twitter.com/1.1//mutes/users/create.json
		Documentation URL: https://dev.twitter.com/rest/reference/post/mutes/users/create
		'''
		payload={
		}
		content = self.request(http_method='POST', payload=payload)
		return content

	def post_mutes_users_destroy(self):
		'''
		Implements https://api.twitter.com/1.1//mutes/users/destroy.json
		Documentation URL: https://dev.twitter.com/rest/reference/post/mutes/users/destroy
		'''
		payload={
		}
		content = self.request(http_method='POST', payload=payload)
		return content

	def get_mutes_users_ids(self):
		'''
		Implements https://api.twitter.com/1.1//mutes/users/ids.json
		Documentation URL: https://dev.twitter.com/rest/reference/get/mutes/users/ids
		'''
		payload={
		}
		content = self.request(http_method='GET', payload=payload)
		return content

	def get_mutes_users_list(self):
		'''
		Implements https://api.twitter.com/1.1//mutes/users/list.json
		Documentation URL: https://dev.twitter.com/rest/reference/get/mutes/users/list
		'''
		payload={
		}
		content = self.request(http_method='GET', payload=payload)
		return content

	def get_users_suggestions_slug(self):
		'''
		Implements https://api.twitter.com/1.1//users/suggestions/slug.json
		Documentation URL: https://dev.twitter.com/rest/reference/get/users/suggestions/slug
		'''
		payload={
		}
		content = self.request(http_method='GET', payload=payload)
		return content

	def get_users_suggestions(self):
		'''
		Implements https://api.twitter.com/1.1//users/suggestions.json
		Documentation URL: https://dev.twitter.com/rest/reference/get/users/suggestions
		'''
		payload={
		}
		content = self.request(http_method='GET', payload=payload)
		return content

	def get_users_suggestions_slug_members(self):
		'''
		Implements https://api.twitter.com/1.1//users/suggestions/slug/members.json
		Documentation URL: https://dev.twitter.com/rest/reference/get/users/suggestions/slug/members
		'''
		payload={
		}
		content = self.request(http_method='GET', payload=payload)
		return content

	def get_favorites_list(self):
		'''
		Implements https://api.twitter.com/1.1//favorites/list.json
		Documentation URL: https://dev.twitter.com/rest/reference/get/favorites/list
		'''
		payload={
		}
		content = self.request(http_method='GET', payload=payload)
		return content

	def post_favorites_destroy(self):
		'''
		Implements https://api.twitter.com/1.1//favorites/destroy.json
		Documentation URL: https://dev.twitter.com/rest/reference/post/favorites/destroy
		'''
		payload={
		}
		content = self.request(http_method='POST', payload=payload)
		return content

	def post_favorites_create(self):
		'''
		Implements https://api.twitter.com/1.1//favorites/create.json
		Documentation URL: https://dev.twitter.com/rest/reference/post/favorites/create
		'''
		payload={
		}
		content = self.request(http_method='POST', payload=payload)
		return content

	def get_lists_list(self):
		'''
		Implements https://api.twitter.com/1.1//lists/list.json
		Documentation URL: https://dev.twitter.com/rest/reference/get/lists/list
		'''
		payload={
		}
		content = self.request(http_method='GET', payload=payload)
		return content

	def get_lists_statuses(self):
		'''
		Implements https://api.twitter.com/1.1//lists/statuses.json
		Documentation URL: https://dev.twitter.com/rest/reference/get/lists/statuses
		'''
		payload={
		}
		content = self.request(http_method='GET', payload=payload)
		return content

	def post_lists_members_destroy(self):
		'''
		Implements https://api.twitter.com/1.1//lists/members/destroy.json
		Documentation URL: https://dev.twitter.com/rest/reference/post/lists/members/destroy
		'''
		payload={
		}
		content = self.request(http_method='POST', payload=payload)
		return content

	def get_lists_memberships(self):
		'''
		Implements https://api.twitter.com/1.1//lists/memberships.json
		Documentation URL: https://dev.twitter.com/rest/reference/get/lists/memberships
		'''
		payload={
		}
		content = self.request(http_method='GET', payload=payload)
		return content

	def get_lists_subscribers(self):
		'''
		Implements https://api.twitter.com/1.1//lists/subscribers.json
		Documentation URL: https://dev.twitter.com/rest/reference/get/lists/subscribers
		'''
		payload={
		}
		content = self.request(http_method='GET', payload=payload)
		return content

	def post_lists_subscribers_create(self):
		'''
		Implements https://api.twitter.com/1.1//lists/subscribers/create.json
		Documentation URL: https://dev.twitter.com/rest/reference/post/lists/subscribers/create
		'''
		payload={
		}
		content = self.request(http_method='POST', payload=payload)
		return content

	def get_lists_subscribers_show(self):
		'''
		Implements https://api.twitter.com/1.1//lists/subscribers/show.json
		Documentation URL: https://dev.twitter.com/rest/reference/get/lists/subscribers/show
		'''
		payload={
		}
		content = self.request(http_method='GET', payload=payload)
		return content

	def post_lists_subscribers_destroy(self):
		'''
		Implements https://api.twitter.com/1.1//lists/subscribers/destroy.json
		Documentation URL: https://dev.twitter.com/rest/reference/post/lists/subscribers/destroy
		'''
		payload={
		}
		content = self.request(http_method='POST', payload=payload)
		return content

	def post_lists_members_create_all(self):
		'''
		Implements https://api.twitter.com/1.1//lists/members/create_all.json
		Documentation URL: https://dev.twitter.com/rest/reference/post/lists/members/create_all
		'''
		payload={
		}
		content = self.request(http_method='POST', payload=payload)
		return content

	def get_lists_members_show(self):
		'''
		Implements https://api.twitter.com/1.1//lists/members/show.json
		Documentation URL: https://dev.twitter.com/rest/reference/get/lists/members/show
		'''
		payload={
		}
		content = self.request(http_method='GET', payload=payload)
		return content

	def get_lists_members(self):
		'''
		Implements https://api.twitter.com/1.1//lists/members.json
		Documentation URL: https://dev.twitter.com/rest/reference/get/lists/members
		'''
		payload={
		}
		content = self.request(http_method='GET', payload=payload)
		return content

	def post_lists_members_create(self):
		'''
		Implements https://api.twitter.com/1.1//lists/members/create.json
		Documentation URL: https://dev.twitter.com/rest/reference/post/lists/members/create
		'''
		payload={
		}
		content = self.request(http_method='POST', payload=payload)
		return content

	def post_lists_destroy(self):
		'''
		Implements https://api.twitter.com/1.1//lists/destroy.json
		Documentation URL: https://dev.twitter.com/rest/reference/post/lists/destroy
		'''
		payload={
		}
		content = self.request(http_method='POST', payload=payload)
		return content

	def post_lists_update(self):
		'''
		Implements https://api.twitter.com/1.1//lists/update.json
		Documentation URL: https://dev.twitter.com/rest/reference/post/lists/update
		'''
		payload={
		}
		content = self.request(http_method='POST', payload=payload)
		return content

	def post_lists_create(self):
		'''
		Implements https://api.twitter.com/1.1//lists/create.json
		Documentation URL: https://dev.twitter.com/rest/reference/post/lists/create
		'''
		payload={
		}
		content = self.request(http_method='POST', payload=payload)
		return content

	def get_lists_show(self):
		'''
		Implements https://api.twitter.com/1.1//lists/show.json
		Documentation URL: https://dev.twitter.com/rest/reference/get/lists/show
		'''
		payload={
		}
		content = self.request(http_method='GET', payload=payload)
		return content

	def get_lists_subscriptions(self):
		'''
		Implements https://api.twitter.com/1.1//lists/subscriptions.json
		Documentation URL: https://dev.twitter.com/rest/reference/get/lists/subscriptions
		'''
		payload={
		}
		content = self.request(http_method='GET', payload=payload)
		return content

	def post_lists_members_destroy_all(self):
		'''
		Implements https://api.twitter.com/1.1//lists/members/destroy_all.json
		Documentation URL: https://dev.twitter.com/rest/reference/post/lists/members/destroy_all
		'''
		payload={
		}
		content = self.request(http_method='POST', payload=payload)
		return content

	def get_lists_ownerships(self):
		'''
		Implements https://api.twitter.com/1.1//lists/ownerships.json
		Documentation URL: https://dev.twitter.com/rest/reference/get/lists/ownerships
		'''
		payload={
		}
		content = self.request(http_method='GET', payload=payload)
		return content

	def get_saved_searches_list(self):
		'''
		Implements https://api.twitter.com/1.1//saved_searches/list.json
		Documentation URL: https://dev.twitter.com/rest/reference/get/saved_searches/list
		'''
		payload={
		}
		content = self.request(http_method='GET', payload=payload)
		return content

	def get_saved_searches_show_id(self):
		'''
		Implements https://api.twitter.com/1.1//saved_searches/show/id.json
		Documentation URL: https://dev.twitter.com/rest/reference/get/saved_searches/show/id
		'''
		payload={
		}
		content = self.request(http_method='GET', payload=payload)
		return content

	def post_saved_searches_create(self):
		'''
		Implements https://api.twitter.com/1.1//saved_searches/create.json
		Documentation URL: https://dev.twitter.com/rest/reference/post/saved_searches/create
		'''
		payload={
		}
		content = self.request(http_method='POST', payload=payload)
		return content

	def post_saved_searches_destroy_id(self):
		'''
		Implements https://api.twitter.com/1.1//saved_searches/destroy/id.json
		Documentation URL: https://dev.twitter.com/rest/reference/post/saved_searches/destroy/id
		'''
		payload={
		}
		content = self.request(http_method='POST', payload=payload)
		return content

	def get_geo_id_place_id(self):
		'''
		Implements https://api.twitter.com/1.1//geo/id/place_id.json
		Documentation URL: https://dev.twitter.com/rest/reference/get/geo/id/place_id
		'''
		payload={
		}
		content = self.request(http_method='GET', payload=payload)
		return content

	def get_geo_reverse_geocode(self):
		'''
		Implements https://api.twitter.com/1.1//geo/reverse_geocode.json
		Documentation URL: https://dev.twitter.com/rest/reference/get/geo/reverse_geocode
		'''
		payload={
		}
		content = self.request(http_method='GET', payload=payload)
		return content

	def get_geo_search(self):
		'''
		Implements https://api.twitter.com/1.1//geo/search.json
		Documentation URL: https://dev.twitter.com/rest/reference/get/geo/search
		'''
		payload={
		}
		content = self.request(http_method='GET', payload=payload)
		return content

	def post_geo_place(self):
		'''
		Implements https://api.twitter.com/1.1//geo/place.json
		Documentation URL: https://dev.twitter.com/rest/reference/post/geo/place
		'''
		payload={
		}
		content = self.request(http_method='POST', payload=payload)
		return content

	def get_trends_place(self):
		'''
		Implements https://api.twitter.com/1.1//trends/place.json
		Documentation URL: https://dev.twitter.com/rest/reference/get/trends/place
		'''
		payload={
		}
		content = self.request(http_method='GET', payload=payload)
		return content

	def get_trends_available(self):
		'''
		Implements https://api.twitter.com/1.1//trends/available.json
		Documentation URL: https://dev.twitter.com/rest/reference/get/trends/available
		'''
		payload={
		}
		content = self.request(http_method='GET', payload=payload)
		return content

	def get_application_rate_limit_status(self):
		'''
		Implements https://api.twitter.com/1.1//application/rate_limit_status.json
		Documentation URL: https://dev.twitter.com/rest/reference/get/application/rate_limit_status
		'''
		payload={
		}
		content = self.request(http_method='GET', payload=payload)
		return content

	def get_help_configuration(self):
		'''
		Implements https://api.twitter.com/1.1//help/configuration.json
		Documentation URL: https://dev.twitter.com/rest/reference/get/help/configuration
		'''
		payload={
		}
		content = self.request(http_method='GET', payload=payload)
		return content

	def get_help_languages(self):
		'''
		Implements https://api.twitter.com/1.1//help/languages.json
		Documentation URL: https://dev.twitter.com/rest/reference/get/help/languages
		'''
		payload={
		}
		content = self.request(http_method='GET', payload=payload)
		return content

	def get_help_privacy(self):
		'''
		Implements https://api.twitter.com/1.1//help/privacy.json
		Documentation URL: https://dev.twitter.com/rest/reference/get/help/privacy
		'''
		payload={
		}
		content = self.request(http_method='GET', payload=payload)
		return content

	def get_help_tos(self):
		'''
		Implements https://api.twitter.com/1.1//help/tos.json
		Documentation URL: https://dev.twitter.com/rest/reference/get/help/tos
		'''
		payload={
		}
		content = self.request(http_method='GET', payload=payload)
		return content

	def get_trends_closest(self):
		'''
		Implements https://api.twitter.com/1.1//trends/closest.json
		Documentation URL: https://dev.twitter.com/rest/reference/get/trends/closest
		'''
		payload={
		}
		content = self.request(http_method='GET', payload=payload)
		return content

	def post_users_report_spam(self):
		'''
		Implements https://api.twitter.com/1.1//users/report_spam.json
		Documentation URL: https://dev.twitter.com/rest/reference/post/users/report_spam
		'''
		payload={
		}
		content = self.request(http_method='POST', payload=payload)
		return content

	def get_collections_list(self):
		'''
		Implements https://api.twitter.com/1.1//collections/list.json
		Documentation URL: https://dev.twitter.com/rest/reference/get/collections/list
		'''
		payload={
		}
		content = self.request(http_method='GET', payload=payload)
		return content

	def get_collections_show(self):
		'''
		Implements https://api.twitter.com/1.1//collections/show.json
		Documentation URL: https://dev.twitter.com/rest/reference/get/collections/show
		'''
		payload={
		}
		content = self.request(http_method='GET', payload=payload)
		return content

	def get_collections_entries(self):
		'''
		Implements https://api.twitter.com/1.1//collections/entries.json
		Documentation URL: https://dev.twitter.com/rest/reference/get/collections/entries
		'''
		payload={
		}
		content = self.request(http_method='GET', payload=payload)
		return content

	def post_collections_create(self):
		'''
		Implements https://api.twitter.com/1.1//collections/create.json
		Documentation URL: https://dev.twitter.com/rest/reference/post/collections/create
		'''
		payload={
		}
		content = self.request(http_method='POST', payload=payload)
		return content

	def post_collections_update(self):
		'''
		Implements https://api.twitter.com/1.1//collections/update.json
		Documentation URL: https://dev.twitter.com/rest/reference/post/collections/update
		'''
		payload={
		}
		content = self.request(http_method='POST', payload=payload)
		return content

	def post_collections_destroy(self):
		'''
		Implements https://api.twitter.com/1.1//collections/destroy.json
		Documentation URL: https://dev.twitter.com/rest/reference/post/collections/destroy
		'''
		payload={
		}
		content = self.request(http_method='POST', payload=payload)
		return content

	def post_collections_entries_add(self):
		'''
		Implements https://api.twitter.com/1.1//collections/entries/add.json
		Documentation URL: https://dev.twitter.com/rest/reference/post/collections/entries/add
		'''
		payload={
		}
		content = self.request(http_method='POST', payload=payload)
		return content

	def post_collections_entries_remove(self):
		'''
		Implements https://api.twitter.com/1.1//collections/entries/remove.json
		Documentation URL: https://dev.twitter.com/rest/reference/post/collections/entries/remove
		'''
		payload={
		}
		content = self.request(http_method='POST', payload=payload)
		return content

	def post_collections_entries_move(self):
		'''
		Implements https://api.twitter.com/1.1//collections/entries/move.json
		Documentation URL: https://dev.twitter.com/rest/reference/post/collections/entries/move
		'''
		payload={
		}
		content = self.request(http_method='POST', payload=payload)
		return content

	def post_collections_entries_curate(self):
		'''
		Implements https://api.twitter.com/1.1//collections/entries/curate.json
		Documentation URL: https://dev.twitter.com/rest/reference/post/collections/entries/curate
		'''
		payload={
		}
		content = self.request(http_method='POST', payload=payload)
		return content








if __name__ == '__main__':
	# Consumer stuff:
	consumer_key = 'RcPVxXd9RqG0lc6ITkZFcImXh' # API Key
	consumer_secret = 'vE95Ub92p621MyyEmJ5ulmXLIi0rRuFi1Z1ux6af51xRUhSvK0' # API Secret	
	key = '4440739934-tOAJNBuWswPGf2WMG52xuo8qZOe1bEW0pbvGgP7' # Test Key
	secret = 'IglPU4pbEwJPaf2grUkFd6jotMH1PW2kbx1x4FvCLzWRl' # Test Secret
	twitter_client = TwitterClient(consumer_key=consumer_key, consumer_secret=consumer_secret, key=key, secret=secret)