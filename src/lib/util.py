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

def obj(t, x):
	return Object(t, x)

def var(x):
	return obj('variable', x)

def dat(x):
	return obj('value', x)

def fun(x):
	return obj('operator', x)

def ind(x):
	return obj('index', x)

def ref(x):
	return obj('pointer', x)

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

def NEG(X):
	for i in range(len(X)):
		if X[i] >= 0: return False
	return True

def POS(X):
	for i in range(len(X)):
		if X[i] < 0: return False
	return True

def ALL(X):
	for i in range(len(X)):
		if X[i] != True:return False
	return True
def SOME(X):
	for i in range(len(X)):
		if X[i] == True:return True
	return False

def MEAN(X):
	if len(X) == 0: return 0
	return TOTAL(X) / len(X)

def TOTAL(X):
	y = 0
	for i in range(len(X)):
		if X[i]: y += 1
	return y

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
