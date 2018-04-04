class Vocabulary(dict):
	def word(self, symbol, name):
		self[symbol] = name
	def create(self, symbols, names):
		for i in range(len(symbols)):
			name = names[i]
			symbol = symbols[i]
			self.word(symbol, name)

class Database(dict):
	def model(self, name, type, index):
		self[name] = {'type': type, 'index': index}
	def create(self, function_names, variable_names):
		for i in range(len(function_names)):
			name = function_names[i]
			self.model(name, 'f', i)
		for i in range(len(variable_names)):
			name = variable_names[i]
			self.model(name, 'v', i)

class Memory(dict):
	def __init__(self):
		self['f'] = []
		self['v'] = []
	def data(self, type, object):
		self[type].append(object)
	def create(self, functions, variables):
		self['f'] = functions
		self['v'] = variables

