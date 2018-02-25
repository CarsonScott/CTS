from Frame import *
from Functions import *

def Object(oclass, index, children):
	frame = Frame('object')
	frame['class'] = oclass
	frame['index'] = index
	frame['children'] = children
	return frame

class Interpreter:

	def __init__(self, structural, functional, rules):
		self.structural = structural
		self.functional = functional
		self.rules = rules

	def compute(self, object, structure):
		P = structure['parents']
		I = object['index']
		if I in P:
			Y = [I]
			C = object['children']
			for child in C:
				V = self.compute(child, structure)
				if V != None: return Y + V
			return [I]
		return None

	def append(self, tree, object, directory):
		O = tree
		history = list()
		indices = list()
		for i in range(1, len(directory)):
			children = O['children']	
			for j in range(len(children)):
				if children[j]['index'] == directory[i]:
					history.append(O)
					indices.append(j)
					O = children[j]
					break
		O['children'].append(object)
		for i in range(len(history)-1, -1, -1):
			history[i]['children'][indices[i]] = O
			O = history[i]
			del history[i]
		return O

	def __call__(self, sentence):
		components = define(mark(sentence, self.structural))
		operations = define(mark(sentence, self.functional))
		model = create(components + operations)
		
		functions = []
		structures = []
		for i in range(len(model)):
			O = model[i]
			if O['class'] == self.rules['structure']['name']:
				structures.append(O)
			else: functions.append(O)

		tree = None
		for i in range(len(structures)-1, -1, -1):
			P = structures[i]['parents']
			if tree == None and len(P) == 0:
				tree = Object(structures[i]['class'], i, list())
			else:
				directory = self.compute(tree, structures[i])
				X = Object(structures[i]['class'], i, list())
				tree = self.append(tree, X, directory)

		for i in range(len(functions)-1, -1, -1):
			P = functions[i]['parents']
			if tree == None and len(P) == 0:
				index = i
				clss = functions[i]['class']
				tree = Object(clss, index, list())
			else:
				directory = self.compute(tree, functions[i])
				tree = self.append(tree, functions[i], directory)
		return tree

