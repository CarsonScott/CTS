from Frames import *

P = Proposition(AND([IN([0, 1, 2, 3, 4]), NOT(IN([0, 1, 2]))]))
Y = P(2)
print(Y)