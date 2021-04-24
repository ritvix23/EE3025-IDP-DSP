import numpy as np

def add(x,y):
	#This fuctions adds two polynomials defined by vectors x and y 
    #z = add(x,y)
    
	import numpy as np
	m = len(x)
	n = len(y)
	if (m == n):
		z = x + y
	elif m > n:
		z = x + np.array([0 for _ in range(m-n) ] + list(y))
	else:
		z = np.array([0 for _ in range(n-m) ] + list(x)) + y
	return z

