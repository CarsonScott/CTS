from Functions import *

def NOT(X):
	if len(X) != 1:
		raise Exception()
	return not X[0]

def AND(X):
	if len(X) != 2:
		raise Exception()
	return X[0] and X[1]
	
def OR(X):
	if len(X) != 2:
		raise Exception()
	return X[0] or X[1]

def EQ(X):
	if len(X) != 2:
		raise Exception()
	return X[0] == X[1]

def MT(X):
	if len(X) != 2:
		raise Exception()
	return X[0] > X[1]

def LT(X):
	if len(X) != 2:
		raise Exception()
	return X[0] > X[1]

def ADD(X):
	if len(X) != 2:
		raise Exception()
	return X[0] + X[1]

def SUB(X):
	if len(X) != 2:
		raise Exception()
	return X[0] - X[1]

def MULT(X):
	if len(X) != 2:
		raise Exception()
	return X[0] * X[1]

def DIV(X):
	if len(X) != 2:
		raise Exception()
	return X[0] / X[1]
