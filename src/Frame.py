class Frame(dict):

	def __init__(self, type):
		self['type'] = type

	def has(self, key):
		return key in list(self.keys())

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

		if isinstance(frame, LogicFrame):
			frame = frame(input)
		return frame

def Operation(function, input):
	frame = LogicFrame('operation')
	frame['function'] = function
	frame['input'] = input
	return frame

def Function(definition):
	frame = LogicFrame('function')
	frame['def'] = definition
	return frame

def Proposition(function):
	frame = LogicFrame('proposition')
	frame['function'] = function
	return frame

def Conjunction(propositions):
	frame = LogicFrame('conjunction')
	frame['propositions'] = propositions
	return frame

def Disjunction(propositions):
	frame = LogicFrame('disjunction')
	frame['propositions'] = propositions
	return frame

def Truth(value):
	frame = LogicFrame('truth')
	frame['value'] = value
	return frame