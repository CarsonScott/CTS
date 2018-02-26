from Functions import *

def NOT(X):
	a = X[0]
	return not a

def AND(X):
	a, b = X[0],X[1]
	return a and b

def OR(X):
	a, b = X[0], X[1]
	return a or b

def EQ(X):
	a, b = X[0], X[1]
	return a == b

# class NOT:
# 	def __init__(self, function):
# 		self.function = function
# 	def __call__(self, value):
# 		return not self.function(value)

# class AND:
# 	def __init__(self, functions):
# 		self.functions = functions
# 	def __call__(self, value):
# 		return UN(istrue)(fcall(self.functions, value))

# class OR:
# 	def __init__(self, functions):
# 		self.functions = functions
# 	def __call__(self, value):
# 		return EX(istrue)(fcall(self.functions, value))

# class EQ:
# 	def __init__(self, value):
# 		self.value = value
# 	def __call__(self, value):
# 		return value == self.value

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

class UN:
	def __init__(self, function):
		self.function = function
	def __call__(self, values):
		return uquantifier(xcall(self.function, values))

class EX:
	def __init__(self, function):
		self.function = function
	def __call__(self, values):
		return equantifier(xcall(self.function, values))
