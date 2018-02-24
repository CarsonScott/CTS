# Constraint-Based Type System

CTS is a python library for scaleable, constraint-based definitions of data types.

__Introduction and Overview__

A Constraint-based type system is a method of defining data types in terms of the conditions and requirements that a given value must meet in order to be considered a valid instance of a specific type. Each variable has a set of constraints, a set of weights, and a threshold, along with its value at any given time. For a value to be accepted by a variable, the sum of weighted outputs from each of the constraint functions associated with the variable must reach its threshold. Constraints are defined as functions that return a truth value for a given input, which in this case is the value held by a certain variable at a given time.

![Variable](https://github.com/CarsonScott/CTS/blob/master/img/constraint_variable.PNG)
	
Constraint functions are distinguished as either base constraints or composite constraints. Base constraints are predefined functions while composite constraints are defined by the composition of multiple other functions. Composite functions can viewed as trees, where each leaf node is a base constraint and each other node is a composite constraint. The depth of a composite constraint is limitless, allowing for possibly infinite hierarchies of functions to be used in defining the conditions of a particular data type.

![Constraints](https://github.com/CarsonScott/CTS/blob/master/img/constraint_hierarchy.PNG)

Constraints may also be defined symbolically using a formal language, providing a method in which a system can scale in real-time via construction of sentences, or strings that conform to the rules of a given language and can be translated by an interpreter into a constraint function. Alternatively, any given constraint function can be translated into a sentence, resulting in a string that, when passed to an interpreter, yields the same constraint function that was originally used to derive the sentence.

![Interpreter](https://github.com/CarsonScott/CTS/blob/master/img/Interpreter.PNG)

A formal language can be understood by an interpreter if it meets a very specific set of criteria. First, the language be able to make references to existing constraints, and thus requires an alphabet of symbols where each constraint is associated with at least one unique symbol, and the use of that symbol in any given sentence is assumed to be in reference to that constraint. Therefore a set of constraint functions can be referenced in a sentence by a set of constraint symbols.
	
The second requirement is the ability to make connections between parts of a sentence via grammatical symbols, which are predefined and unchanging (as apposed to the constraint alphabet, which grows with each new constraint function added to a set). In other words, a set of grammar rules distinguish the way in which two constraints that are connected by a grammar symbol relate to one another. Relations may be hierarchical or lateral, where hierarchical relations denote membership (A contains B), and lateral relations denote logical entailment (A then B), conjunction (A and B), disjunction (A or B), among other connectives.

The last requirement is the ability to distinguish whether a given sentence follows a set of combination rules, or specific ways in which the symbols of a sentence are arranged. More specifically, there must be a set of rules for determining how the various constraint symbols and grammar symbols may relate to one another in a sentence, in order for the interpreter to successfully rewrite the sentence as a constraint function. This is the final step in converting a sentence, as well as the most important property of a formal language in this context. If the interpreter attempts to convert a sentence that does not conform to the combination rules, the resulting function is likely not to operate in the way it was meant to, leading to error in future applications of the constraint, as well as structural problems that could potentially prevent the system from executing.


__Frames and Interpretation__

Frames are objects that convey descriptive information about other objects to an interpreter. Every interpreter has the ability to process information described in a frame via rules that are predefined and dictate the computational steps taken by the interpreter when given a frame. Instructional frames are unique in that they provide descriptions of rules that, when received by an interpreter, can direct its actions to achieve some desired output. Due to the malleability of their functional characteristics, interpreters can meet the requirements of a  formal language through the application of instructional frames to direct its actions when processing an input.

