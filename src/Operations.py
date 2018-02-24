from Functions import fcall

def UNI(values, proposition=None):
	if proposition == None: X = values
	else: X = xcall(proposition, values)
	return False not in X

def EXI(values, proposition=None):
	if proposition == None: X = values
	else: X = xcall(proposition, values)
	return True in X

class NOT:
	def __init__(self, function):
		self.function = function
	def __call__(self, value):
		return not self.function(value)

class AND:
	def __init__(self, functions):
		self.functions = functions
	def __call__(self, value):
		return UNI(fcall(self.functions, value))

class OR:
	def __init__(self, functions):
		self.functions = functions
	def __call__(self, value):
		return EXI(fcall(self.functions, value))

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