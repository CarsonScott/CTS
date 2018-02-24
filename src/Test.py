from Interpreter import *
from Functions import *

constraints = [AND([IN([0, 1, 2, 3, 4]), NOT(IN([0, 1, 2]))])]
interpreter = Interpreter(constraints)

frame = Proposition(0)
output = interpreter(4, frame)

print(output)