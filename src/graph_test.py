from Graph import *
from Operator import MT, LT, EQ

graph = Graph()

# create 5 variables
graph.create('a b c d', 'number')
graph.set('a', 34)
graph.set('b', 4)
graph.set('c', 23)
graph.set('d', 11)
graph.set('e', 1)

# create 3 operators
graph.create('more less equal', 'operator')
graph.set('equal',EQ)
graph.set('more', MT)
graph.set('less', LT)

# create 4 links between variables
graph.link('a', 'b')
graph.link('b', 'c')
graph.link('c', 'd')
graph.link('d', 'e')

# label links with operators
graph.generate(['more', 'less', 'equal'])

# display graph model
model = graph.model()
print(model)