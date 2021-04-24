
#THIS PROGRAM GENERATES THE CHEBYSCHEV POLYNOMIAL COEFFICIENTS OF ORDER N
import numpy as np
def cheb(N):
	import numpy as np
	v = np.array([1,0])
	u = np.array([1])
	if N == 0 : return u
	if N == 1 : return v
	
	for i in range(N-1):
		temp = np.array([2,0])
		p = np.convolve(temp,v)
		m = len(p)
		n = len(u)
		
		w = p + np.array([0 for _ in range(m-n) ] + list(u))
		
		u = v 
		v = w

	return w

