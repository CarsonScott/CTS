# Constraint-Based Type Systems

CTS is a python library for scaleable, constraint-based definitions of data types.

__Overview__

A Constraint-based type system is a method of defining data types in terms of the conditions and requirements that a given value must meet in order to be considered a valid instance of a specific type. Each variable has a set of constraints, a set of weights, and a threshold, along with its value at any given time. For a value to be accepted by a variable, the sum of weighted outputs from each of the constraint functions associated with the variable must reach its threshold. Constraints are defined as functions that return a truth value for a given input, which in this case is the value held by a certain variable at a given time.
	
Constraint functions are distinguished as either base constraints or composite constraints. Base constraints are predefined functions while composite constraints are defined by the composition of multiple other functions. Composite functions can viewed as trees, where each leaf node is a base constraint and each other node is a composite constraint. The depth of a composite constraint is limitless, allowing for possibly infinite hierarchies of functions to be used in defining the conditions of a particular data type.

Constraints may also be defined symbolically using a formal language, providing a method in which a system can scale in real-time via construction of sentences, or strings that conform to the rules of a given language and can be translated by an interpreter into a constraint function. Alternatively, any given constraint function can be translated into a sentence, resulting in a string that, when passed to an interpreter, yields the same constraint function that was originally used to derive the sentence.
