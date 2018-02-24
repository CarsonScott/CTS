from Interpreter import *
from Constraints import *

constraints = [AND([IN([0, 1, 2, 3, 4]), NOT(IN([0, 1, 2]))])]
interpreter = Interpreter(constraints)

frame = Proposition(0)
output = interpreter(3, frame)

print(output)