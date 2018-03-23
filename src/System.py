from Memory import *
from Operator import *
from Functions import *

def create_tree(children, index, objects):
	tree = []
	for i in range(len(children[index])):
		child = children[index][i]
		if len(children[child]) > 0:
			tree.append(create_tree(children, child, objects))
		else:tree.append(objects[child][0])
	return tree

class System:

	def __init__(self):
		self.vocabulary = Vocabulary()
		self.database = Database()
		self.memory = Memory()
		self.script = []
		self.inputs = []
		self.fun(None, '.id', ID)
		self.fun(None, '.set', SET)
		self.fun(None, '_open', None)
		self.fun(None, '_close', None)

	def __setitem__(self, variable, value):
		model = self._model(variable)
		self.memory[model['type']][model['index']] = value
	def __getitem__(self, variable):
		model = self._model(variable)
		return self.memory[model['type']][model['index']]
	def __call__(self, inputs):
		return
	
	def _word(self, symbol):
		return self.vocabulary[symbol]
	def _model(self, word):
		return self.database[word]
	def _data(self, model):
		return self.memory[model['type']][model['index']]

	def fun(self, symbol, name, operator=None):
		self.vocabulary.word(symbol, name)
		self.memory.data('f', operator)
		self.database.model(name, 'f', len(self.memory['f'])-1) 
	def var(self, symbol, value=None):
		self.vocabulary.word(symbol, symbol)
		self.memory.data('v', value)
		self.database.model(symbol, 'v', len(self.memory['v'])-1)
	
	def add_input(self, variable):
		self.inputs.append(variable)
	def add_statement(self, statement):
		self.script.append(statement)

	def update(self, values):
		for i in range(len(values)):
			self[self.inputs[i]] = values[i]
	
	def compute(self, inputs):
		self.update(inputs)
		outputs = []
		for i in range(len(self.script)):
			tree = self.parse(self.script[i])
			output = self.execute(tree)
			outputs.append(output)
		return outputs

	def parse(self, statement):
		symbols = keys(self.vocabulary)
		
	# retreive the set of all variable and function symbols 
		v_symbols = []
		f_symbols = []
		statement = revise(statement)
		for i in range(len(symbols)):
			symbol = symbols[i]
			model = self._model(self._word(symbol))
			if model['type'] == 'f':
				f_symbols.append(symbols[i])
			elif model['type'] == 'v':
				v_symbols.append(symbols[i])

	# store the position of each function symbol in the statement
		boundaries = []
		for i in range(len(statement)):
			if statement[i] in f_symbols:
				name = self._word(statement[i])
				boundaries.append((name, i))

	# store the string between each pair of consequtive functions
		strings = []
		indices = []
		for i in range(1, len(boundaries)):
			index1 = boundaries[i-1][1]+1
			index2 = boundaries[i][1]-1
			string = substring(statement, index1, index2+1)
			if string != '':
				strings.append(string)
				indices.append([index1, index2])

	# assign an encapsulation marker to each element
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

	# create an object for each element pair that reflects encapsulation 
		ordered = []
		indices = []
		for i in range(len(elements)):
			indices.append(elements[i][1])
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
					model = self._model(previous_name)
					objects.append((previous_name, (previous, index)))
			else:
				names.append(name)
				indices.append(index)

	# create a relation for each object pair that reflects containment
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

	# construct a symbol tree that reflects the containment hierarchy
		return create_tree(children, len(children)-1, objects)

	def execute(self, tree):
	# store the inputs and operators from the tree
		x = list()
		if len(tree) == 1:
			f = '.id'
			x.append(tree[0])
		elif len(tree) == 2:
			f = tree[0]
			x.append(tree[1])
		elif len(tree) == 3:
			f = tree[1]
			x.append(tree[0])
			x.append(tree[2])

	# execute/replace the trees with their outputs and retrieve/replace the variables with their stored data
		for i in range(len(x)):
			if f != '.set' and f != '.if':
				if isinstance(x[i], list):x[i] = self.execute(x[i])
				elif isinstance(x[i], str):x[i] = self._data(self._model(x[i]))
			elif f == '.set' and i == 0:
				x[i] = self._model(x[i])['index']
			elif f == '.if' and x[0] == False:
				x[i] = None
		
	# compute/produce the output of the tree
		if f == '.set':
			x.insert(0, self.memory['v'])
		if f == '.if':
			y = x[1]
		else:
			f = self._data(self._model(f))
			y = f(x)
		return y
