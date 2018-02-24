from Frames import *

proposition = Proposition(AND([IN([0, 1, 2, 3, 4]), NOT(IN([0, 1, 2]))]))
output = interpret(proposition, 3)
print(output)