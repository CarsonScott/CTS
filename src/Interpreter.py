from Functions import *
from Frame import *

class Interpreter:
	def __init__(self, functions):
		self.functions = functions

	def __call__(self, input, frame):
		T = frame['type']

		if T == 'truth':
			frame = frame['value']

		elif T == 'Function':
			D = frame['def']
			frame = Truth(D(input))

		elif T == 'operation':
			X = frame['input']
			F = frame['function']
			frame = Truth(F(X))

		elif T == 'proposition':
			I = frame['index']
			F = self.functions[I]
			frame = Operation(F, input)
	
		elif T == 'conjunction':
			P = frame['propositions']
			F = Function(AND(P))
			frame = Operation(F, input)

		elif T == 'disjunction':
			P = frame['propositions']
			F = Function(OR(P))
			frame = Operation(F, input)

		if not isinstance(frame, bool):
			frame = self(input, frame)
		
		return frame
