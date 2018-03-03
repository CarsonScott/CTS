from System import *

def Kernel(width, height):
	system = System()

	system.fun('&', 'and', AND)
	system.fun('>', 'more', MT)
	system.fun('<', 'less', LT)
	system.fun('+', 'plus', ADD)
	system.fun(':', '.set', SET)
	system.fun('?', '.if', None)
	system.fun('(', '_open', None)
	system.fun(')', '_close', None)

	system.var('w', width)
	system.var('h', height)
	system.var('x', 0)
	system.var('y', 0)
	system.var('tx', 0)
	system.var('ty', 0)
	system.var('dx', 0)
	system.var('dy', 0)
	system.var('def', 0)
	system.var('inc', 1)
	system.var('dec', -1)
	system.var('up', (0, 1))
	system.var('down', (0, -1))
	system.var('left', (-1, 0))
	system.var('right', (1, 0))
	
	system.inputs = ['tx', 'ty']
	system.script = ['((x > tx) ? (dx : dec))','((x < tx) ? (dx : inc))',
		 	 	     '((y > ty) ? (dy : dec))','((y < ty) ? (dy : inc))',
		 		     '(x : (x + dx))','(y : (y + dy))',
		 		     '(dx : def)','(dy : def)']
	return system

