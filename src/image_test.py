from Graph import *
from Operator import LEFTOF, RIGHTOF, ABOVE, BELOW
from random import randrange as rr
from math import sqrt

LETTERS = 'abcdefghijklmnopqrtstuvwxyz'
NUMBERS = '0123456789'

class Point(dict):
	def __init__(self, x, y):
		self['x'] = x
		self['y'] = y

def distance(p1, p2):
	x1, y1 = p1['x'], p1['y']
	x2, y2 = p2['x'], p2['y']
	return sqrt(pow(x2-x1, 2) + pow(y2-y1, 2))

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

def randstr(alphabet, size):
	string = ''
	for i in range(size):
		string += alphabet[rr(len(alphabet))]
	return string

# create 10x10 grid of 0's
grid = Grid(10, 10, 0)

# add random 1's to the grid
for i in range(len(grid)):
	for j in range(len(grid[i])):
		if rr(10) < 2:
			grid[i][j] = 1

# create graph
graph = Graph()

# add 4 operators to the graph
graph.create('leftof rightof above below', 'operator')
graph.set('leftof',LEFTOF)
graph.set('rightof', RIGHTOF)
graph.set('above', ABOVE)
graph.set('below', BELOW)

# add nodes to the graph from 1's in the grid
for i in range(len(grid)):
	for j in range(len(grid)):
		if grid[i][j] == 1:
			graph.set(randstr(LETTERS, 5), Point(j, i))

# create links between nearby nodes
for i in graph.keys():
	for j in graph.keys():
		if i != j:
			a = graph.get(i)
			b = graph.get(j)
			d = distance(a, b)
			if d <= 2:
				graph.link(i, j)

# label links with operators
graph.generate(['leftof', 'rightof', 'above', 'below'])

# display model
model = graph.model()
print(model)

