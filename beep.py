import os
import time

t0 = time.time()

def alert():
	return os.system('spd-say -t female3 "your code has finished"')

def duration():
	t1 = time.time()
	total = t1-t0
	return print("Your code took %f seconds" % total)
