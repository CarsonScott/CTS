from Frame import *
from Functions import *
from Operations import *

class Interpreter:
	def __init__(self, F, V):
		self.system = F
		self.variables = V

	def compute(self, object, input):
		P = input['parents']
		I = object['index']
		if I in P:
			Y = [I]
			C = object['children']
			for child in C:
				V = self.compute(child, input)
				if V != []: return Y + V
			return [I]
		return []

	def append(self, tree, object, directory):
		O = tree
		history = list()
		indices = list()
		for i in range(1, len(directory)):
			children = O['children']	
			for j in range(len(children)):
				if children[j]['index'] == directory[i]:
					history.append(O)
					indices.append(j)
					O = children[j]
					break
		O['children'].append(object)
		for i in range(len(history)-1, -1, -1):
			history[i]['children'][indices[i]] = O
			O = history[i]
			del history[i]
		return O

	def construct(self, model):
		structures = []
		functions = []
		variables = []
		for i in range(len(model)):
			O = model[i]
			if O['type'] == 'structure':
				structures.append(O)
			elif O['type'] == 'function':
				functions.append(O)
			else: variables.append(O)
		elements = variables + functions + structures

		tree = None
		for i in range(len(elements)-1, -1, -1):
			P = elements[i]['parents']
			if tree == None and len(P) == 0:
				C = elements[i]['type']
				N = elements[i]['class']
				tree = Object(C, N, i, list())
			else:
				directory = self.compute(tree, elements[i])
				C = elements[i]['type']
				N = elements[i]['class']
				X = Object(C, N, i, list())
				tree = self.append(tree, X, directory)
		return tree

	def convert(self, object):
		T = object['type']
	
		if T == 'structure':
			I = None
			C = object['children']
			for i in range(len(C)):
				C[i] = self.convert(C[i])	
				if C[i]['type'] == 'value':
					C[i] = C[i]['value']
				elif C[i]['type'] == 'function':
					C[i] = C[i]['definition']
					I = i
			F = C[I]
			del C[I]
			object = Statement(F, C)

		elif T == 'function':
			N = object['name']
			F = self.system[N]
			object = Function(F)

		elif T == 'variable':
			N = object['name']
			V = self.variables[N]
			object = Value(V)
		return object

	def __call__(self, sentence):
		indices = []
		sentence = revise(sentence)
		boundaries = mark(sentence, self.system)
		for i in range(len(boundaries)):
			indices.append(boundaries[i][1])
	
		s = ''
		names = []
		elements = []
		for i in range(len(sentence)):
			if i not in indices:
				s += sentence[i]
			elif s != '':
				elements.append(['variable', i-len(s)])
				elements.append(['/variable', i-1])
				names.append(s)
				s = ''
		
		elements = define(elements)
		for i in range(len(elements)):
			elements[i] = [names[i], elements[i][1], 'variable']
		model = create(elements + define(boundaries))
		
		tree = self.construct(model)
		output = self.convert(tree)
		return output

def Create(alphabet):
	system = dict()
	for i in range(len(alphabet)):
		s = alphabet[i]
		name = s['name']
		sign = s['sign']
		if isinstance(sign, list):
			system[sign[0]] = name
			system[sign[1]] = '/' + name
		else:
			function = s['function'] 
			system[sign] = '/' + name + '/' 
			system[name] = function
	return system