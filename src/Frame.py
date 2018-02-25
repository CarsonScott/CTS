class Frame(dict):

	def __init__(self, type):
		self['type'] = type

	def __call__(self, input):
		return

	def has(self, key):
		return key in list(self.keys())