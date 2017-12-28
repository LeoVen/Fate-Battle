from random import randint
from classes import *
from stats import *

def select():
	#hid = randint(0, 6)
	hid = 0
	return Hero(  hid, 	stats[hid][0], stats[hid][1], stats[hid][2], stats[hid][3], stats[hid][4], 
						stats[hid][5], stats[hid][6], stats[hid][7], stats[hid][8], stats[hid][9])

	

		