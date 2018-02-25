def fcall(functions, value):
	return [f(value) for f in functions]

def xcall(function, values):
	return [function(x) for x in values]

def uquantifier(X):
	return False not in X

def equantifier(X):
	return True in X

def istrue(x):
	return x == True

def isfalse(x):
	return x == False

def subset(X, s, e):
	Y = []
	for i in range(s, e):
		Y.append(X[i])
	return Y

def substring(X, s, e):
	Y = ''
	for i in range(s, e):
		Y += X[i]
	return Y

def keys(d):
	return list(d.keys())

def match(start, end):
	return start == end[1:]

def contains(range1, range2):
	i1, f1 = range1
	i2, f2 = range2
	return i1 < i2 and f1 > f2

def children(index, relations):
	y = []
	for i in range(len(relations)):
		if relations[i][0] == index:
			y.append(relations[i][1])
	return y

def parents(index, relations):
	y = []
	for i in range(len(relations)):
		if relations[i][1] == index:
			y.append(relations[i][0])
	return y

def mark(sentence, vocabulary):
	markers = []
	for i in range(len(sentence)):
		c = sentence[i]
		if c in keys(vocabulary):
			s = vocabulary[c]
			markers.append((s, i))
	return markers

def define(boundaries):
	history = []
	indices = []
	objects = []
	for i in range(len(boundaries)):
		label, index = boundaries[i]
		if label[0] == '/':
			if match(history[len(history)-1], label):
				C = history[len(history)-1]
				D = (indices[len(indices)-1], index)
				del history[len(history)-1]
				del indices[len(indices)-1]	
				objects.append((C, D))
		else:
			history.append(label)
			indices.append(index)
	return objects

def compose(objects):
	relations = []
	for i in range(len(objects)):
		for j in range(i, len(objects)):
			if i != j:
				Ri = objects[i][1]
				Rj = objects[j][1]

				if contains(Ri, Rj):
					relations.append((i,j))
				elif contains(Rj, Ri):
					relations.append((j,i))
	outputs = []
	for i in range(len(objects)):
		symbol = objects[i][0]
		domain = objects[i][1]
		indices = children(i, relations)
		outputs.append([symbol, domain, indices])
	return outputs

class Structure(dict):
	def __init__(self, type, value):
		self['type'] = type
		self['data'] = value

def construct(sentence, objects, ):
	requirements = []
	outputs = objects
	for i in range(len(objects)):
		if not isinstance(objects[i], Structure):
			elements = objects[i][2]
			
			if len(elements) == 0:
				start, end = objects[i][1]
				value = substring(sentence, start+1, end)
				outputs[i] = Structure('model', value)
			else:
				unassigned = []
				for j in range(len(elements)):
					if not isinstance(elements[j], Structure):
						object = objects[elements[j]]
						if isinstance(object, Structure):
							elements[j] = object
						else:
							unassigned.append(j)
				requirements.append(unassigned)
				outputs[i][2] = elements
				
				if len(unassigned) == 0:
					values = outputs[i][2]
					outputs[i] = Structure('model', values)

	if len(requirements) > 0:
		outputs = construct(sentence, outputs)
	return outputs