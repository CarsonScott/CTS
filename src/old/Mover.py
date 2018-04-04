from System import *
from random import randrange as rr

def random(range):
	return rr(range)

def Mover():
	system = System()
	system.fun('.', 'get', GET)
	system.fun('~', 'call', CALL)
	system.fun('!', 'not', NOT)
	system.fun('&', 'and', AND)
	system.fun('|', 'or', OR)
	system.fun('>', 'more', MT)
	system.fun('<', 'less', LT)
	system.fun('=', 'equal', EQ)
	system.fun('+', 'plus', ADD)
	system.fun('*', 'mult', MULT)
	system.fun('-', 'sub', SUB)
	system.fun('/', 'div', DIV)
	system.fun(':', '.set', SET)
	system.fun('?', '.if', None)
	system.fun('(', '_open', None)
	system.fun(')', '_close', None)

	system.var('pattern', None)
	system.var('output', None)
	system.var('none', 0)
	system.var('horizontal', 1)
	system.var('vertical', 2)
	system.var('up', 0)
	system.var('down', 1)
	system.var('left', 2)
	system.var('right', 3)
	system.var('random', random)
	system.var('range', 4)

	system.inputs = ['pattern']
	system.script = [
		'((pattern = horizontal) ? (output : right))',
		'((pattern = vertical) ? (output : down))'
		'((pattern = none) ? (output : (random ~ range))'
	]
	return system
