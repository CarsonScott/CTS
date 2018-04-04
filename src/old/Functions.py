def keys(x):
	return list(x.keys())

def is_num(x):
	try:float(x)
	except:return False
	return True

def to_num(x):
	if '.' in str(x):
		return float(x)
	else:return int(x)

def contains(r1, r2):
	i1, f1 = r1
	i2, f2 = r2
	return i1 < i2 and f1 > f2

def substring(x, i, j):
	y = ''
	for k in range(i, j):
		y += x[k]
	return y

def revise(x):
	y = ''
	for i in range(len(x)):
		if x[i] != ' ':y += x[i]
	return y

def sort(x):
	values = x
	indices = [i for i in range(len(x))]
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

def is_true(x):
	return x == True

def is_false(x):
	return x == False

def all_to(O, x):
	return [o(x) for o in O]

def to_all(o, X):
	return [o(x) for x in X]

def for_all(o, x):
	return False not in to_all(o, x)

def for_some(o, x):
	return True in to_all(o, x)


