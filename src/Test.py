from Frames import *

prop = Proposition(AND([IN([0, 1, 2, 3, 4]), NOT(IN([0, 1, 2]))]))
output = prop(1)
print(output)