from Variable import *
from Constraints import *

def Bool():
	variable = Variable()
	variable.add_constraint(TypeConstraint(bool), 1)
	variable.set_threshold(1)
	return variable

def Int():
	variable = Variable()
	variable.add_constraint(TypeConstraint(int), 1)
	variable.set_threshold(1)
	return variable

def Float():
	variable = Variable()
	variable.add_constraint(TypeConstraint(float), 1)
	variable.set_threshold(1)
	return variable

def String():
	variable = Variable()
	variable.add_constraint(TypeConstraint(str), 1)
	variable.set_threshold(1)
	return variable