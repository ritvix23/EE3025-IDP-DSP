def lattice(c,v):
	#The function
    #computes the lattice parameters K and the ladder parameters C for the
    #system function H(z) = N(z)/D(z), where both the numerator and denominator
    #are of the same order
    
	u = v[::-1]
	m = len(v)
	K[m-2] = v[m-1]
	C[m-1] = c[m-1]
	
	while (m>1 and K[m-2] != 1):
		c = c - C[m-1]*u
		v = (v - (K[m-2])*u)/(1 - K[m-1]**2)
		m = m-1
		v = v[0:m]
		c = c[0:m]
		
		u = v[::-1]
		if m > 1: K[m-2] = v[m-1]
		C[m-1] = c[m-1]
	
	return C,K

