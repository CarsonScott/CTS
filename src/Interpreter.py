from Functions import *
from Operator import *

class Interpreter:
	def __init__(self, system):
		self.system = system

	def parse(self, sentence):
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
		return tree

	def execute(self, tree):
		operator = Operator()
		for i in range(len(tree)):
			if isinstance(tree[i], list):
				operator['x'].append(self.execute(tree[i]))
			
			else:
				name = tree[i]
				model = self.system.database[name]
				data = self.system.reference(name)

				if model['type'] == 'f':
					operator['f'] = data
				elif model['type'] == 'v':
					operator['x'].append(data)
		
		return operator.compute()

def create_tree(children, index, objects):
	tree = []
	for i in range(len(children[index])):
		child = children[index][i]
		if len(children[child]) > 0:
			tree.append(create_tree(children, child, objects))
		else:
			tree.append(objects[child][0])
	return tree
	