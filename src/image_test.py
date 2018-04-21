from Graph import *
from Agent import *
from Operator import LEFTOF, RIGHTOF, ABOVE, BELOW
from random import randrange as rr
from math import sqrt

class ImageAgent(Agent):
	
	def update(self):
		i = self.i

		Ni = []
		for j in range(len(self.N)):
			if self.N[j] not in self.V:
				Ni.append(self.N[j])

		y = None
		if len(Ni) == 0:
			if i not in self.V:
				y = self.H[len(self.H)-1]
				
		self.H.append(i)
		if i not in self.V:
			self.V.append(y)

		self.set(y)

		# else:


		# k = None
		# for i in range(len(N)):


		# for c in range(len(N)):
		# 	if N[c] != None:
		# 		j = N[c]

		# if j != None:
		# 	y = j
		# else:
		# 	y = self.history[len(self.history)-2]
		# return y


# create 10x10 grid of 0's
grid = Grid(9, 9, 0)

# add random 1's to the grid
for i in range(len(grid)):
	for j in range(len(grid[i])):
		if rr(10) < 3:
			grid[i][j] = 1

# create graph
graph = Graph()

# add nodes to the graph from 1's in the grid
for i in range(len(grid)):
	for j in range(len(grid)):
		if grid[i][j] == 1:
			name = str(len(graph.keys()))
			graph.set(name, PVector(j, i))

# create links between nearby nodes
for i in graph.keys():
	for j in graph.keys():
		if i != j:
			a = graph.get(i)
			b = graph.get(j)
			d = distance(a, b)
			if d <= 2:
				graph.link(i, j)

# add 2 operators to the graph
graph.op('offx', OFFX)
graph.op('offy', OFFY)

# label links with operators
ops = ['offx', 'offy']
graph.generate(ops, 'function')

# display model
grid.print()
print()

model = graph.model

K = model.keys()
i = K[0]
Ki = model.neighbors(i)
j = Ki[0]
Yij = model.get(i, j)
Yji = model.get(j, i)

agent = ImageAgent(model)
agent.set('1')

x = i
c = 0
p = None

done = False
while not done:
	x = agent.i
	agent.update()

	c += 1
	if c > 100:
		done = True
	print(x, agent.V)



# keys = Keys(model)
# for i in Keys(model):
# 	for j in model.neighbors(i):
# 		print(i + ' ' + j + ' ' + str(model[i][j]))
