from Frame import *
from Functions import *
from Operations import *

class Interpreter:
	def __init__(self, system):
		self.system = system

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
		sentence = revise(sentence)

		symbols = keys(self.system.vocabulary)
		v_symbols = []
		f_symbols = []

		for i in range(len(symbols)):
			symbol = symbols[i]
			model = self.system.translate(symbol) 		
			if model['type'] == 'f':f_symbols.append(symbols[i])
			elif model['type'] == 'v':v_symbols.append(symbols[i])

		boundaries = []
		for i in range(len(sentence)):
			if sentence[i] in f_symbols:
				symbol = self.system.vocabulary[sentence[i]]
				boundaries.append((symbol, i))

		strings = []
		indices = []
		for i in range(1, len(boundaries)):
			index1 = boundaries[i-1][1]+1
			index2 = boundaries[i][1]-1
			string = substring(sentence, index1, index2+1)
			if string != '':
				strings.append(string)
				indices.append([index1, index2])

		elements = []
		for i in range(len(strings)):
			index1, index2 = indices[i]
			elements.append((strings[i], index1))
			elements.append(('/'+strings[i], index2))

		for i in range(len(boundaries)):
			name, index = boundaries[i]
			elements.append((name, index))
			if name[0] != '_':
				elements.append(('/'+name, index))

		indices = []
		for i in range(len(elements)):
			indices.append(elements[i][1])

		ordered = []
		indices = sort(indices)
		for i in indices:
			ordered.append(elements[i])
		elements = ordered
		print(elements)
		names = []
		indices = []
		objects = []
		for i in range(len(elements)):
			name = elements[i][0]
			index = elements[i][1]
			
			if name[0] == '_':
				if name == '_open':
					indices.append(index)
					names.append(name)		
				if name == '_close':
					previous = indices[len(indices)-1]
					del indices[len(indices)-1]
					del names[len(names)-1]
					objects.append((None, (previous, index)))
			
			elif name[0] == '/':
				previous_name = names[len(names)-1]
				if name == '/' + previous_name:
					previous = indices[len(indices)-1]
					del indices[len(indices)-1]
					del names[len(names)-1]
					model = self.system.database[previous_name]
					objects.append((previous_name, (previous, index)))
			else:
				names.append(name)
				indices.append(index)
		print(objects)						

		children = []
		for i in range(len(objects)):
			children.append([])
			for j in range(len(objects)):
				range1 = objects[i][1]
				range2 = objects[j][1]
				if contains(range1, range2):
					children[i].append((j))

		for i in range(len(children)):
			indices = children[i]
			for j in range(len(indices)):
				for k in range(len(indices)):
					child = indices[j]
					if indices[k] in children[child]:
						indices[k] = None
			children[i] = indices

		for i in range(len(children)):
			indices = []
			for j in range(len(children[i])):
				if children[i][j] != None:
					indices.append(children[i][j])
			children[i] = indices

		tree = create_tree(children, len(children)-1, objects)
		print(tree)

def create_tree(children, index, objects):
	tree = []
	for i in range(len(children[index])):
		child = children[index][i]
		if len(children[child]) > 0:
			tree.append(create_tree(children, child, objects))
		else:
			tree.append(objects[child][0])
	return tree
		# # for i in range(len(boundaries)):
		# # 	indices.append(boundaries[i][1])
	
		# s = ''
		# names = []
		# elements = []
		# for i in range(len(sentence)):
		# 	if i not in indices:
		# 		s += sentence[i]
		# 	elif s != '':
		# 		elements.append(['variable', i-len(s)])
		# 		elements.append(['/variable', i])
		# 		names.append(s)
		# 		s = ''

		# elements = define(elements)
		# for i in range(len(elements)):
		# 	elements[i] = [names[i], elements[i][1], 'variable']

		# model = create(elements + define(boundaries))
		
		# for m in model:
		# 	print(m)

		# tree = self.construct(model)
		# output = self.convert(tree)
		# return output

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
			system[sign] = '/' + name + '/' 
			function = s['function'] 
			system[name] = function
	return system