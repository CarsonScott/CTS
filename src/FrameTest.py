from Frame import Frame

def Not(x):
	return not x[0]

def And(x):
	return x[0] and x[1]

def Or(x):
	return x[0] or x[1]

class Size:
	def __init__(self, s):
		self.size = s
		
	def __call__(self, x):
		return len(x) == self.size

class Constraint(dict):
	def __init__(self, k, p):
		self['k'] = k
		self['p'] = p

class Operation(dict):
	def __init__(self, f):
		self['f'] = f
		self['x'] = list()
		self['c'] = list()

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

class Negation(Operation):
	def __init__(self):
		super().__init__(Not)
		self['c'].append(Constraint('x', Size(1)))

class Conjunction(Operation):
	def __init__(self):
		super().__init__(And)
		self['c'].append(Constraint('x', Size(2)))

class Disjunction(Operation):
	def __init__(self):
		super().__init__(Or)
		self['c'].append(Constraint('x', Size(2)))

con = Conjunction()
con['x'].append(True)
con['x'].append(True)
print(con.valid())

# def And(a, b):
# 	return a and b

# def Or(a, b):
# 	return a or b

# def Variable(T, D):
# 	frame = dict()
# 	frame['class'] = 'variable'
# 	frame['type'] = T
# 	frame['value'] = D
# 	return frame

# def Operation(D, F):
# 	frame = dict()
# 	frame['class'] = 'operation'
# 	frame['X'] = X
# 	frame['F'] = F
# 	return frame

# def Composition(O, C):
# 	frame = dict()
# 	frame['class'] = 'composition'
# 	frame['O'] = O
# 	frame['C'] = C
# 	return frame

# def execute(F):
# 	C = F['class']
# 	if C == 'composition':
# 		x = F['O']
# 		f = F['C']
# 		for i in range(len(x)):
# 			x[i] = execute(x[i])
# 		F = f(x)
# 	elif C == 'operation':
# 		x = F['X']
# 		f = F['F']
# 		F = f(x)
# 	return F

# def bool_type(x):
# 	return x['type'] == 'bool'
# def true_value(x):
# 	return x['value'] == True
# def conjunction(X):
# 	return False not in X

# X = Variable('bool', True)
# O = [Operation(X, bool_type),
# 	 Operation(X, true_value)]
# C = Composition(O, conjunction)

# print(execute(C))
