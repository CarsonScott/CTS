from math import sqrt

class Link(dict):
	def __init__(self, a, b, x):
		self['a'] = a
		self['b'] = b
		self['x'] = x

class PVector(dict):
	
	def __init__(self, x, y):
		self['x'] = x
		self['y'] = y

class Grid(list):
	
	def __init__(self, w, h, v=None):
		for i in range(h):
			self.append([])
			for j in range(w):
				self[i].append(v)

	def print(self):
		for i in range(len(self)):
			string = ''
			for j in range(len(self[i])):
				string += str(self[i][j]) + ' '
			print(string)

class Dict(dict):

	def create(self, k, v=None):
		for i in k:
			self.set(i, v)
	
	def keys(self):
		return list(super().keys())

	def has(self, k):
		return k in self.keys()

	def set(self, k, x):
		self[k] = x

class Graph(Dict):

	def link(self, a, b, x=None):
		if not self.has(a):
			self.set(a, Dict())
		if not self.has(b):
			self.set(b, Dict())

		if not self[a].has(b):
			self[a].set(b, [])
		self[a][b].append(x)

	def links(self, key):
		return list(self[key].keys())

	def get_link(self, a, b):
		if b in self.paths(a):
			return self[a][b]
		return None

def sort(d):
	keys = list(d.keys())
	vals = []
	for i in range(len(keys)):
		k = keys[i]
		vals.append(d[k])

	if len(keys) <= 1:
		return keys

	done = False
	while not done:
		done = True
		for i in range(len(keys)-1):
			k1 = keys[i]
			k2 = keys[i+1]

			v1 = vals[i]
			v2 = vals[i+1]

			if v2 < v1:
				done = False
				keys[i] = k2
				vals[i] = v2
				keys[i+1] = k1
				vals[i+1] = v1
	return keys

def distance(p1, p2):
	x1, y1 = p1['x'], p1['y']
	x2, y2 = p2['x'], p2['y']
	return sqrt(pow(x2-x1, 2) + pow(y2-y1, 2))

def parse(string, char=[' ']):
	char.append(None)
	data = []
	s = ''
	for i in range(len(string)+1):
		if i < len(string):
			c = string[i]
		else:c = None

		if c in char:
			if s != '':
				data.append(s)
				s = ''
		else:s += c
	return data

def Keys(data):
	return list(data.keys())

def gather(data, variables=[]):
	if len(variables) == 0:
		variables = Keys(data)
	values = []
	for i in variables:
		values.append(data.get(i))
	return values

def has(data, variable):
	return variable in Keys(data)

def compute(inputs, functions):
	outputs = []
	for i in range(len(functions)):
		outputs.append(functions[i](inputs))
	return outputs

def select(options, functions, selection):
	scores = []
	for i in range(len(functions)):
		scores.append(functions[i](options))
	return selection(scores)

def istrue(X):
	Y = []
	for i in range(len(X)):
		if X[i] == True:
			Y.append(i)
	return Y

def direct(links):
	sizes = dict()
	for i in range(len(links)):
		a, b = links[i]
		if a not in sizes:
			sizes[a] = 0
		if b not in sizes:
			sizes[b] = 0
		sizes[a] += 1
		sizes[b] += 1

	for i in range(len(links)):
		a, b = links[i]
		if sizes[a] < sizes[b]:
			links[i] = [b, a]
	return links

def merge(string1, string2, char=''):
	return string1 + char + string2
	
def unpack(graph):
	keys = []
	links = []
	for i in Keys(graph):
		keys.append(i)
		for j in Keys(graph[i]):
			if j not in keys:
				keys.append(j)
			links.append([i, j, graph[i][j]])
	return keys, links


