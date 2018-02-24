from Operations import *

class Frame(dict):

	def __init__(self, type):
		self['type'] = type

	def __call__(self, input):
		frame = self
		
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
			F = frame['function']
			frame = Operation(F, input)

		elif T == 'conjunction':
			P = frame['propositions']
			F = Function(AND(P))
			frame = Operation(F, input)

		elif T == 'disjunction':
			P = frame['propositions']
			F = Function(OR(P))
			frame = Operation(F, input)

		print(frame)	
		if not isinstance(frame, bool):
			frame = frame(input)
		
		return frame

def Function(definition):
	f = Frame('function')
	f['def'] = definition
	return f

def Operation(function, input):
	f = Frame('operation')
	f['function'] = function
	f['input'] = input
	return f

def Proposition(function):
	f = Frame('proposition')
	f['function'] = function
	return f

def Conjunction(propositions):
	f = Frame('conjunction')
	f['propositions'] = propositions
	return f

def Disjunction(propositions):
	f = Frame('disjunction')
	f['propositions'] = propositions
	return f

def Truth(value):
	f = Frame('truth')
	f['value'] = value
	return f

