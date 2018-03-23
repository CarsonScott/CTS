from System import *

class Object(System):
	def __init__(self):
		super().__init__()
		self.weights = []

	def __call__(self, inputs):
		outputs = self.compute(inputs)
		for i in range(len(outputs)):
			outputs[i] *= self.weights[i]
		return sum(outputs)

	def add_statement(self, statement, weight):
		super().add_statement(statement)
		self.weights.append(weight)

o = Object()

o.fun('(', '_open')
o.fun(')', '_close')

o.fun('!', 'not', NOT)
o.fun('&', 'and', AND)
o.fun('|', 'or', OR)

o.var('a')
o.var('b')
o.var('c')

o.add_input('a')
o.add_input('b')
o.add_input('c')

o.add_statement('(a & (!b))', 0.5)
o.add_statement('(b | c)', 0.5)


y = o([True, False, True])
print(y)