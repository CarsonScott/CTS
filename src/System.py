from Memory import *
from Operator import *
from Functions import *

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

	def _word(self, symbol):
		return self.vocabulary[symbol]
	def _model(self, word):
		return self.database[word]
	def _data(self, model):
		return self.memory[model['type']][model['index']]

	def __setitem__(self, variable, value):
		model = self._model(variable)
		self.memory[model['type']][model['index']] = value
		
	def __getitem__(self, variable):
		model = self._model(variable)
		return self.memory[model['type']][model['index']]

	def fun(self, symbol, name, operator):
		self.vocabulary.word(symbol, name)
		self.memory.data('f', operator)
		self.database.model(name, 'f', len(self.memory['f'])-1) 

	def var(self, symbol, value):
		self.vocabulary.word(symbol, symbol)
		self.memory.data('v', value)
		self.database.model(symbol, 'v', len(self.memory['v'])-1) 

	def compute(self, inputs):
		self.update(inputs)
		outputs = []
		for i in range(len(self.script)):
			outputs.append(self.execute(self.parse(self.script[i])))
		return outputs

	def update(self, values):
		for i in range(len(values)):
			self[self.inputs[i]] = values[i]

	def parse(self, sentence):
		sentence = revise(sentence)
		symbols = keys(self.vocabulary)
		v_symbols = []
		f_symbols = []

		for i in range(len(symbols)):
			symbol = symbols[i]
			model = self._model(self._word(symbol))
			if model['type'] == 'f':f_symbols.append(symbols[i])
			elif model['type'] == 'v':v_symbols.append(symbols[i])

		boundaries = []
		for i in range(len(sentence)):
			if sentence[i] in f_symbols:
				name = self._word(sentence[i])
				boundaries.append((name, i))

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
					model = self._model(previous_name)
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
		x = []
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

		for i in range(len(x)):
			if f == '.set' and i == 0:
				x[i] = self._model(x[i])['index']
			elif f == '.if' and x[0] == False:
				x[i] = None
			else:
				if isinstance(x[i], list):
					x[i] = self.execute(x[i])
				elif isinstance(x[i], str):
					x[i] = self._data(self._model(x[i]))

		if f != '.if':
			if f == '.set':
				x.insert(0, self.memory['v'])
			f = self._data(self._model(f))
			y = f(x)
		else: y = x[1]
		return y
		# for i in range(len(tree)):
		# 	if isinstance(tree[i], list):
		# 		x.append(self.execute(tree[i]))
		# 	else:
		# 		name = tree[i]
		# 		model = self._model(name)
		# 		data = self._data(self._model(name))

		# 		if model['type'] == 'f':
		# 			f = data
		# 		elif model['type'] == 'v':
		# 			x.append(data)

		# 		if name[0] == '.':
		# 			ismember = True
		
		# operator = Operator(f)
		# return operator(x)	

