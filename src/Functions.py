def Con(X):
	for i in range(len(X)):
		if X[i] == False:
			return False
	return True

def Dis(X):
	for i in range(len(X)):
		if X[i] == True:
			return True
	return False
