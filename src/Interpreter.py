from Frame import *
from Functions import *
from Operations import *

def Object(T, N, I, C):
	frame = Frame(T)
	frame['class'] = N
	frame['index'] = I
	frame['children'] = C
	return frame

class Interpreter:

	def __init__(self, structural, functional, rules):
		self.structural = structural
		self.functional = functional
		self.rules = rules
		self.variables = []
		self.functions = []

	def compute(self, object, input):
		P = input['parents']
		I = object['index']
		if I in P:
			Y = [I]
			C = object['children']
			print(I)
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
		functions = []
		structures = []
		variables = []
		for i in range(len(model)):
			O = model[i]
			if O['type'] == 'structure':
				structures.append(O)
			elif O['type'] == 'function':
				functions.append(O)
			else:
				variables.append(O)
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
		# elements = functions + variables
		# for i in range(len(elements)):
		# 	P = elements[i]['parents']
		# 	directory = self.compute(tree, elements[i])
		# 	tree = self.append(tree, elements[i], directory)

		# for i in range(len(variables)):
		# 	P = variables[i]['parents']
		# 	directory = self.compute(tree, variables[i])
		# 	tree = self.append(tree, variables[i], directory)
	def convert(self, object):
		T = object['type']

		if T == 'structure':
			C = object['children']
			for i in range(len(C)):
				C[i] = self.convert(C[i])

		elif T == 'function':
		
	def __call__(self, sentence):
		sentence = revise(sentence)
		components = define(mark(sentence, self.structural))
		operations = define(mark(sentence, self.functional))
		boundaries = mark(sentence, self.structural) + mark(sentence, self.functional)

		indices = []
		for i in range(len(boundaries)):
			indices.append(boundaries[i][1])
	
		string = ''
		names = []
		elements = []
		for i in range(len(sentence)):
			if i not in indices:
				string += sentence[i]
			elif string != '':
				elements.append(['variable', i-len(string)])
				elements.append(['/variable', i-1])
				names.append(string)
				string = ''

		elements = define(elements)
		for i in range(len(elements)):
			elements[i] = [names[i], elements[i][1], 'variable']
		model = create(elements + operations + components)
		
		tree = self.construct(model)
		return tree
		# rules = {'and':AND, 'or':OR}
		# output = convert(sentence, tree, rules)
		# return output

