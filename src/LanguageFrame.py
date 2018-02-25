from Frame import *
from Functions import *

class LanguageFrame(Frame):

	def __call__(self, input, language=None):
		frame = self

		T = frame['type']
		if T == 'sentence':
			language = frame['language']
			R = language['structure']
			M = mark(input, R)
			frame = Demarcation(M)

		elif T == 'demarcation':
			M = frame['markers']
			O = define(M)
			frame = Definition(O)

		elif T == 'definition':
			O = frame['objects']
			E = compose(O)
			frame = Composition(E)

		elif T == 'composition':
			E = frame['elements']
			C = construct(input, E)
			frame = Model(C[len(C)-1])

		if frame['type'] != 'model':
			frame = frame(input, language)
		return frame

def Demarcation(markers):
	frame = LanguageFrame('demarcation')
	frame['markers'] = markers
	return frame

def Definition(objects):
	frame = LanguageFrame('definition')
	frame['objects'] = objects
	return frame

def Composition(elements):
	frame = LanguageFrame('composition')
	frame['elements'] = elements
	return frame

def Sentence(language):
	frame = LanguageFrame('sentence')
	frame['language'] = language
	return frame

def Model(composition):
	frame = LanguageFrame('model')
	frame['data'] = composition
	return frame

def Language(structure_symbols, function_symbols):
	frame = Frame('language')
	frame['structure'] = structure_symbols
	frame['function'] = function_symbols
	return frame

# def Definition(string):
# 	frame = LanguageFrame('definition')
# 	frame['string'] = string
# # 	return frame

# def Boundary(initial, final):
# 	frame = LanguageFrame('boundary')
# 	frame['start'] = initial
# 	frame['end'] = final
# 	return frame

# def Template(name, sign):
# 	frame = LanguageFrame('template')
# 	frame['name'] = name
# 	frame['sign'] = sign
# 	return frame

