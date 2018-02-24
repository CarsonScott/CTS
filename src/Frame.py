def Frame(type):
	f = dict()
	f['type'] = type
	return f
def Operation(function, input):
	f = Frame('operation')
	f['function'] = function
	f['input'] = input
	return f
def Proposition(index):
	f = Frame('proposition')
	f['index'] = index
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