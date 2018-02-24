def fcall(F, x):
	return [f(x) for f in F]

def xcall(f, X):
	return [f(x) for x in X]

def uquantifier(X):
	return False not in X

def equantifier(X):
	return True in X

def istrue(x):
	return x == True

def isfalse(x):
	return x == False