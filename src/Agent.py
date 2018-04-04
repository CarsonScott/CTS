from Graph import *

class Agent(Graph):

	def __init__(self):
		super().__init__()
		self.function = None

	def interpret(self, string):
		objects = parse(string, ['.'])
		elements = []
		for i in range(len(objects)):
			objects[i] = parse(objects[i], ['/'])
			if len(objects[i]) == 1:
				objects[i] = objects[i][0]
		return objects

	def state(self, key, state):
		self.set(merge(key, 'S', '.'), state)

	def check(self, key):
		return self.get(merge(key, 'S', '.'))
	
	def move(self, key):
		return self.get(merge(key, 'N', '.'))

	def reset(self):
		for i in self.get('nodes'):
			self.set(i + '.S', False)

	def construct(self, graph):
		keys, links = unpack(graph)
		self.arr('nodes', keys)
		self.arr('links', links)

		for i in range(len(keys)):
			key = merge(keys[i], 'S', '.')
			self.set(key, False)
			key = merge(keys[i], 'N', '.')
			self.arr(key, [])
			if keys[i] in Keys(graph):
				self.set(key, Keys(graph[keys[i]]))

		for i in range(len(links)):
			a,b,f = links[i]
			key = merge(a, b, '/')
			function = [[], 'total']
			for j in f:
				function[0].append([[a, b], j])
			self.set(key, function, 'function')

	def run(self, key, origin=True):
		X = self.move(key)		
		K = []
		Y = []

		for i in X:
			s = self.check(i)
			if s == False:
				x = self.get(merge(key, i, '/'))
				y = self.execute(x)
				Y.append(y)
				K.append(i)

		for i in range(len(Y)):
			if Y[i] == True: 
				Y[i] = self.run(K[i], False)
		if len(Y) == 0: y = 1
		else: y = sum(Y)
		
		self.state(key, y)
		return self.check(key)