class Size:
	def __init__(self, s):
		self.size = s
		
	def __call__(self, x):
		return len(x) == self.size

class Constraint(dict):
	def __init__(self, k, p):
		self['k'] = k
		self['p'] = p

def InputSize(Constraint):
	def __init__(self, s):
		super().__init__('x',[Size(s)])

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
