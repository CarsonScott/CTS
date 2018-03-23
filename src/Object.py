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
