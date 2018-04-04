from Data import *

def label(message):
	labels = []
	for i in message:
		labels.append(i.isupper())
	return labels

class Parser:

	def __call__(self, message):
		labels = []
		message = parse(message, [';'])
		for i in range(len(message)):
			message[i] = parse(message[i], [' ', ','])
			labels.append(label(message[i]))

		functions = []
		variables = []		
		for i in range(len(labels)):
			for j in range(len(labels[i])):
				if labels[i][j]:
					functions.append(message[i][j].lower())
					variables.append([])
				else:variables[len(functions)-1].append(message[i][j])
		
		objects = []
		for i in range(len(functions)):
			objects.append(Object('function', [variables[i], functions[i]]))
		return objects

