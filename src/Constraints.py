class InclusionConstraint:
	def __init__(self, values):
		self.values = values
	def __call__(self, value):
		return value in self.values

class TypeConstraint:
	def __init__(self, type):
		self.type = type
	def __call__(self, value):
		return isinstance(value, self.type)
