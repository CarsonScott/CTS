def is_true(x):
	return x == True
def is_false(x):
	return x == False
def all_to(O, x):
	return [o(x) for o in O]
def to_all(o, X):
	return [o(x) for x in X]
def for_all(o, x):
	return False not in to_all(o, x)
def for_some(o, x):
	return True in to_all(o, x)

class Operator(dict):

	def __init__(self, f=None):
		self['f'] = f
		self['x'] = list()
		self['c'] = list()
		self['k'] = list()

	def call(self, i):
		k = self['k'][i]
		f = self['c'][i]
		x = self[k]
		return f(x)

	def rate(self):
		output = []
		for i in range(len(self['c'])):
			y = self.call(i)
			output.append(y)
		return output

	def valid(self):
		rate = self.rate()
		return for_all(is_true, rate)

	def apply(self, k, c):
		self['k'].append(k)
		self['c'].append(c)

	def compute(self):
		if self.valid():
			x = self['x']
			f = self['f']
			return f(x)
	
	def __call__(self, x):
		self['x'] = x
		return self.compute()

class ALLTO(Operator):
	def compute(self):
		return all_to(self['f'], self['x'])
class TOALL(Operator):
	def compute(self):
		return to_all(self['f'], self['x'])
class FORALL(Operator):
	def compute(self):
		return for_all(self['f'], self['x'])
class FORSOME(Operator):
	def compute(self):
		return for_some(self['f'], self['x'])

def TRUE(X):
	if len(X) != 1:raise Exception()
	return X[0] == True
def FALSE(X):
	if len(X) != 1:raise Exception()
	return X[0] == False
def NOT(X):
	if len(X) != 1:raise Exception()
	return not X[0]
def AND(X):
	if len(X) != 2:raise Exception()
	return X[0] and X[1]	
def OR(X):
	if len(X) != 2:raise Exception()
	return X[0] or X[1]
def EQ(X):
	if len(X) != 2:raise Exception()
	return X[0] == X[1]
def MT(X):
	if len(X) != 2:raise Exception()
	return X[0] > X[1]
def LT(X):
	if len(X) != 2:raise Exception()
	return X[0] < X[1]
def ADD(X):
	if len(X) != 2:raise Exception()
	return X[0] + X[1]
def SUB(X):
	if len(X) != 2:raise Exception()
	return X[0] - X[1]
def MULT(X):
	if len(X) != 2:raise Exception()
	return X[0] * X[1]
def DIV(X):
	if len(X) != 2:raise Exception()
	return X[0] / X[1]
def LEN(X):
	if len(X) != 1: raise Exception()
	return len(X[0])
def ID(X):
	if len(X) != 1: raise Exception()
	return X[0]
def GET(X):
	if len(X) != 2: raise Exception()
	return X[0][X[1]]
def SET(X):
	if len(X) != 3: raise Exception()
	X[0][X[1]] = X[2]