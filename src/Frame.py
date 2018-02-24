def Frame(type):
	f = dict()
	f['type'] = type
	return f

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
	