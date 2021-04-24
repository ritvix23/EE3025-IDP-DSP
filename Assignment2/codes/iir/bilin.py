from add import *
from polypower import *

def bilin(p,om):
	import numpy as np
	#This function transforms the stable bandpass  filter obtained
    #from the Chebyschev approximation to the equivalent bandpass
    #digital filter using the bilinear transformation
    #[dignum,digden,G_bp] = bilin(p,om)
    #H_bp(s) = G_bp*num(s)/den(s) is the analog bandpass filter
    #obtained through the Chebyschev filter design
    #H(z) = G*dignum(z)/digden(z) is digital bandpass filter
    #obtained from H_bp(s) by substituting s = (z-1)/(z+1)
    #G is obtained from the condition H(om) = 1
	
	N = len(p)
	const = np.array([-1,1])
	v = 1
	if N > 2:
		for i in range(N-1):
			v = np.convolve(const,v)
			v = add(v,p[i+1]*polypower([1,1],i+1))
		digden  = v
	elif N == 2:
		M = len(v)
		v[M-2] = v[M-2] + p[N-1]
		v[M-1] = v[M-1] + p[N-1]
		digden = v
	else:
		digden = p
	dignum = polypower([-1,0,1],(N-1)//2)
	G_bp = abs(np.polyval(digden, np.exp(-1j*om))/np.polyval(dignum,np.exp(-1j*om)))
	
	return dignum , digden, G_bp

