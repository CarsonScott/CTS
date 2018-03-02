from Operator import *

class Template:

	def __setitem__(self, v, x):
		self.variables[v] = x

	def __init__(self, s):
		self.relations = []
		self.functions = []
		self.variables = [None for i in range(s)]

	def relate(self, i, j, f):
		self.relations.append([i, j])
		self.functions.append(f)

	def compute(self):
		output = []
		for i in range(len(self.relations)):
			i1, i2 = self.relations[i]
			x1 = self.variables[i1]
			x2 = self.variables[i2]
			f = self.functions[i]
			f['x'] = x1, x2
			if f.valid():
				y = f.compute()
				output.append(y)
		return output

def create(f, s):
	O = Operator()
	O['f'] = f
	O.apply('x', sizeof(s))
	return O

class sizeof:
	def __init__(self, s):
		self.size = s
	def __call__(self, x):
		return len(x) == self.size

Add = create(AND, 2)

tem = Template(2)
tem.relate(0, 1, Add)
tem[0] = False
tem[1] = True
print(tem.compute())


