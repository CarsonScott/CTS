def isnumber(x):
	try:
		int(x)
		return True
	except:
		return False

def num(x):
	if '.' in str(x):
		return float(x)
	else:
		return int(x)

def keys(d):
	return list(d.keys())

def substring(X, s, e):
	Y = ''
	for i in range(s, e):
		Y += X[i]
	return Y

def contains(range1, range2):
	i1, f1 = range1
	i2, f2 = range2
	return i1 < i2 and f1 > f2

def revise(string):
	output = ''
	for i in range(len(string)):
		if string[i] != ' ':
			output += string[i]
	return output

def create_tree(children, index, objects):
	tree = []
	for i in range(len(children[index])):
		child = children[index][i]
		if len(children[child]) > 0:
			tree.append(create_tree(children, child, objects))
		else:tree.append(objects[child][0])
	return tree

def sort(X):
	values = X
	indices = [i for i in range(len(X))]
	done = False
	while not done:
		done = True
		for i in range(1, len(values)):
			if values[i] < values[i-1]:
				done = False
				value = values[i-1]
				values[i-1] = values[i]
				values[i] = value
				index = indices[i-1]
				indices[i-1] = indices[i]
				indices[i] = index
	return indices

def extract(space, kernel):
	xi = kernel['x'] - round(kernel['w']/2)
	xf = kernel['x'] + round(kernel['w']/2)
	yi = kernel['y'] - round(kernel['h']/2)
	yf = kernel['y'] + round(kernel['h']/2)
	subspace = []
	for y in range(yi, yf+1):
		row = []
		for x in range(xi, xf+1	):
			row.append(space[y][x])
		subspace.append(row)
	return subspace