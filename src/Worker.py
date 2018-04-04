from Agent import *
from random import randrange as rr
class Worker(Agent):

	def __init__(self, isize=None, bsize=None):
		super().__init__()
		self.function = None
		self.inputs = []
		self.buffer = []
		self.isize = isize
		self.bsize = bsize
		self.step = 0

	def send(self, data):
		self.buffer.append(data)
		if len(self.buffer) > self.bsize:
			error = len(self.buffer) - self.bsize
			del self.buffer[:error]

	def update(self, time, output=''):
		self.step = time
		self.send(output)

	def __call__(self, time, inputs=None):
		output = self.function(inputs)
		return output

class Detector(Worker):

	def unpack(self, data):
		if isinstance(data, list):
			for i in range(len(data)):
				if not isinstance(data[i], str):
					data[i] = self.unpack(data[i])
			return data		
		elif isinstance(data, dict):
			return self.unpack(Keys(data))
		return data

	def initialize(self, data):
		K = self.unpack(data)
		print(K)
		X = []
		for i in K:
			self.set(i, data[i])
			self.set(i+'.s', 0)

	def observe(self, time, inputs):		
		X = []
		string = ''
		for i in range(len(inputs)):
			if inputs[i] != ' ':
				x = inputs[i]
				string += x
			elif string != '':
				X.append(string)
				string = ''

		for i in range(len(X)):
			self.state(X[i], 1)
		self.update(time)

	def state(self, key, state):
		self.set(key + '.s', state)


worker = Detector(10, 10)
worker.initialize({'and':1, 'very':2, 'cool':2})
for i in range(109):
	print(worker.buffer)
	X = ['and','very','cool']
	x = X[rr(len(X))]
	worker.observe(i, x)
	print(worker.get('and'))