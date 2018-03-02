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
		else:
			tree.append(objects[child][0])
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