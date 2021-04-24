def polypower(v,N):
	import numpy as np
	y = np.array([1])
	for i in range(N): y = np.convolve(y,v)
	return y

