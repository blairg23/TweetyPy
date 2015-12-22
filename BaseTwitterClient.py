
class BaseTwitterClient():
	def __init__(self):
		pass
	def authenticate(self):
		'''Authenticate against the Twitter API and check the return to make sure we have a valid connection, return true or false'''
		raise NotImplementedError()
	def request(self):
		'''Make an HTTP request'''
		raise NotImplementedError()