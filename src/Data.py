from lib.util import *

class Object:
	def __init__(self, d_type, value):
		self.type = d_type
		self.value = value

class Operator:
	def __init__(self, function):
		self.function = function
	def __call__(self, values):
		return self.function(values)

class Data:

	def __init__(self):
		self.variables = dict()
		self.values = list()
		self.types = list()

	def keys(self):
		return Keys(self.variables)

	def ind(self, key, index):
		self.set(key, index, 'index')

	def ref(self, key, reference):
		self.set(key, reference, 'reference')
	
	def fun(self, key, function, inputs):
		self.set(key, [inputs, function], 'function')

	def op(self, key, operator):
		self.set(key, Operator(operator), 'operator')
	
	def num(self, key, number):
		self.set(key, number, 'number')

	def str(self, key, string):
		self.set(key, string, 'string')

	def arr(self, key, array):
		self.set(key, array, 'array')	

	def get(self, index):
		index = self.translate(index)
		return self.values[index].value

	def type(self, index):
		index = self.translate(index)
		return self.values[index].type

	def settype(self, key, type):	
		index = self.translate(key)
		self.values[key].type = type
	
	def getall(self, type):
		indices = []
		keylist = keys(self.variables)
		for i in range(len(keylist)):
			if self.type(keylist[i]) == type:
				indices.append(keylist[i])
		return indices

	def all(self, index):
		for i in range(len(list(self.variables.values()))):
			if i == index:
				return self.variables[i]

	def getlist(self, keys):
		output = []
		for i in range(len(keys)):
			output.append(self.get(keys[i]))
		return output

	def set(self, variable, value=None,type=None):
		if not has(self.variables, variable):
			self.values.append(Object(value, type))
			self.variables[variable] = len(self.values)-1
		index = self.variables[variable]
		self.values[index].value = value
		if type != None:
			self.values[index].type = type

	def execute(self, function):
		inputs = function[0]
		operator = function[1]
		for i in range(len(inputs)):
			if isinstance(inputs[i], str):
				inputs[i] = self.get(inputs[i])
			if isinstance(inputs[i], list):
				inputs[i] = self.execute(inputs[i])
		if isinstance(operator, str):
			operator = self.get(operator)
		return operator(inputs)

	def inputs(self, variables):
		self.arguments = variables

	def update(self, inputs):
		for i in range(len(inputs)):
			self.set(self.arguments[i], inputs[i])

	def translate(self, index):
		if isinstance(index, str):
			index = self.variables[index]
		return index

	def create(self, string, type=None):
		x = parse(string)
		for i in range(len(x)):
			self.set(x[i], None, type)

	def convert(self, data):
		if not isinstance(data, Object):
			if isinstance(data, str):
				data = Object('reference', data)
			elif isinstance(data, int) or isinstance(data, float):
				data = Object('number', data)
			elif isinstance(data, list):
				data = Object('array', data)
			elif isinstance(data, Operator):
				data = Object('operator', data)

		types = ['index', 'reference', 
				 'number', 'string', 
				 'operator', 'array', 
				 'function']

		T = data.type
		X = data.value
		x = X
		if T in types:
			I = types.index(T)
			if I == 0 or I == 1:
				i = self.translate(X)
				x = self.convert(self.get(i))
			if I == 2 or I == 3 or I == 4:
				x = X
			if I == 5:
				x = []
				for i in range(len(X)):
					x.append(self.convert(X[i]))
			if I == 6:
				f = Object('reference', X[0])
				v = Object('array', X[1])
				f = self.convert(f)
				v = self.convert(v)
				x = f(v)

			if isinstance(x, Object):
				return self.convert(x)
		return x

	def save(self, file):
		file = open(file, 'w')
		string = ''
		for k in self.keys():
			i = self.translate(k)
			t = self.type(k)
			x = self.get(k)

			if t == 'operator':
				x = k

			string += '<'
			string += str(k) + ','
			string += str(i) + ','
			string += str(t) + ','
			string += str(x) + '>;'
			string += '\n'
		file.write(string)
		file.close()