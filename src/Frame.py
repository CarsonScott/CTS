class Frame(dict):

	def __init__(self, type):
		self['type'] = type

	def has(self, key):
		return key in list(self.keys())

	def __call__(self, input):
		frame = self
		T = frame['type']

		if T == 'value':
			return frame['value']
	
		elif T == 'Function':
			D = frame['definition']
			frame = Value(D(input))

		elif T == 'operation':
			X = frame['input']
			F = frame['function']
			# frame = Truth(F(X))
			frame = Value(F(X))

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

		if isinstance(frame, Frame):
			frame = frame(input)
		return frame

def Operation(function, input):
	frame = Frame('operation')
	frame['function'] = function
	frame['input'] = input
	return frame

def Function(definition):
	frame = Frame('function')
	frame['definition'] = definition
	return frame

def Proposition(function):
	frame = Frame('proposition')
	frame['function'] = function
	return frame

def Conjunction(propositions):
	frame = Frame('conjunction')
	frame['propositions'] = propositions
	return frame

def Disjunction(propositions):
	frame = Frame('disjunction')
	frame['propositions'] = propositions
	return frame

def Value(value):
	frame = Frame('value')
	frame['value'] = value
	return frame