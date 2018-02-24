from Functions import *

def CALL(F, x):
	return [f(x) for f in F]

class NOT:
	def __init__(self, function):
		self.function = function
	def __call__(self, value):
		return not self.function(value)

class AND:
	def __init__(self, functions):
		self.functions = functions
	def __call__(self, value):
		return False not in CALL(self.functions, value)

class OR:
	def __init__(self, functions):
		self.functions = functions
	def __call__(self, value):
		return True in CALL(self.functions, value)

class EQ:
	def __init__(self, value):
		self.value = value
	def __call__(self, value):
		return value == self.value

class MT:
	def __init__(self, value):
		self.value = value
	def __call__(self, value):
		return value > self.value

class LT:
	def __init__(self, value):
		self.value = value
	def __call__(self, value):
		return value < self.value

class IN:
	def __init__(self, values):
		self.values = values
	def __call__(self, value):
		return value in self.values