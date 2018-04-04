from Kernel import *
from Classifier import *
from Mover import *
from random import randrange as rr

space = []
count = 0
for i in range(100):
	space.append([])
	for j in range(100):
		if rr(100) < 20:
			space[i].append(1)
		else:
			space[i].append(0)

patterns = [
	[[0, 0, 0],
	 [0, 0, 0],
	 [0, 0, 0]],

	[[0, 0, 0],
	 [1, 1, 1],
	 [0, 0, 0]],

	[[0, 1, 0],
	 [0, 1, 0],
	 [0, 1, 0]]]

system = Kernel(3, 3, patterns)
system['x'] = 20
system['y'] = 20

mover = Mover()

target = [50, 40]
for i in range(1000):
	input = extract(space, system)
	system.compute(target + [input])
	mover.compute([system['output']])

	target = [system['x'], system['y']]
	output = mover['output']
	if output == 0:
		target[1] = system['y'] -1
	elif output == 1:
		target[1] = system['y'] +1
	elif output == 2:
		target[0] = system['x'] -1
	elif output == 3:
		target[0] = system['x'] +1

	print(i, '	', system['output'])
