class Operator(dict):

	def __init__(self):
		self['x'] = list()
		self['f'] = None
		self['c'] = None

	def valid(self):
		for c in self['c']:
			p = c['p']
			k = c['k']
			y = p(self[k])
			if not y: return False
		return True

	def compute(self):
		f = self['f']
		x = self['x']
		return f(x)

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