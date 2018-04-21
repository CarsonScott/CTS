from lib.util import Dict, Graph, Link, sort

class Agent:

	def compute_error(self, key):
		return pow(len(self.history[key]) - len(self.children[key]), 2)

	def compute_rating(self, key, depth):
		error = self.compute_error(key)
		if depth > 0 and len(self.children[key]) > 0:
			for i in self.model.links(key):
				error += self.compute_rating(i, depth-1)
		return error
	
	def __init__(self, model, thresh, depth):
		self.place = None
		self.thresh = thresh
		self.depth = depth
		self.model = model
		self.log = list()
		self.roots = list()
		self.leaves = list()
		self.children = Dict()
		self.parents = Dict()
		self.history = Dict()

		for i in model.keys():
			self.children[i] = model.links(i)
			self.parents[i] = []
			self.history[i] = []

		for i in model.keys():
			for j in model[i].keys():
				if i not in self.parents[j]:
					self.parents[j].append(i)

		for i in self.children.keys():
			if len(self.children[i]) == 0:
				self.leaves.append(i)
			if len(self.parents[i]) == 0:
				self.roots.append(i)

	def reset(self):
		self.place = None
		for i in self.history.keys():
			self.history[i] = []
		self.log = []

	def update(self, place):
		if self.place != None:
			if place not in self.history[self.place]:
				self.history[self.place].append(place)
		self.log.append(place)
		self.place = place
		
		i = place
		Hi = self.history[i]
		Pi = self.parents[i]
		Ci = self.children[i]
		Ri = Dict()

		for j in range(len(Ci)):
			c = Ci[j]
			if c not in Hi:
				e = self.compute_rating(c, self.depth)
				if e > self.thresh:
					Ri[c] = e
		
		if len(Ri) == 0:
			if i not in self.roots:
				y = self.log[len(self.log)-2]
				del self.log[len(self.log)-1]
			else:y = None		
		else:
			Ki = sort(Ri)
			y = Ki[len(Ki)-1]
		return y
	
	def run(self):
		i = 0
		x = None
		done = False
		while not done:
			if x == None:
				x = self.roots[i]
			y = agent.update(x)
			if y != None: x = y
			else:
				i += 1
				x = None
				if len(self.roots) == i:
					done = True
				else: x = self.roots[i]
