from Functions import Con, Dis
from Frame import *

class Interpreter:
	def __init__(self, functions=list()):
		self.functions = functions

	def add_function(self, function):
		self.functions.append(function)

	def __call__(self, input, frame):
		T = frame['type']
	
		if T == 'truth':
			return frame['value']
		elif T == 'operation':
			X = frame['input']
			F = frame['function']
			frame = Truth(F(X))
		elif T == 'proposition':
			I = frame['index']
			F = self.functions[I]
			frame = Operation(F, input)
		else:
			Y = []
			P = frame['propositions']
			for i in range(len(P)):
				Y.append(self(input, P[i]))
			if T == 'conjunction':
				frame = Operation(Con, Y)
			if T == 'disjunction':
				frame = Operation(Dis, Y)
		return self(input, frame)
