def lpbp(p,Omega0,B,Omega_p2):
	import numpy as np
	#This function transforms the lowpass stable filter obtained
    #from the Chebyschev approximation to the bandpass
    #equivalent
    #[num,den,G] = lpbp(p,Omega0,B,Omega_p2)
    #Omega0 and B are the lowpass-bandpass transformation parameters
    #and Omega_p2 is the lower limit of the passband, used
    #to evaluate the gain G_bp
    #H(s) = G/p(s) is the stable low pass Cheybyschev approximation
    #Hbp(s) = G_bp*num(s)/den(s) is the corresponding bandpass stable
    #filter
     
	N = len(p)
	const = np.array([1, 0, Omega0**2])
	v = np.array([1, 0, Omega0**2])
	
	if N > 2:
		for i in range(N-1):
			M = len(v)
			v[M-i-2] = v[M-i-2] + p[i+1]*(B**(i+1))
			if i < N-2:
				v = np.convolve(const,v)
		den = v
		
	elif N == 2:
		M = len(v)
		v[M-2] = v[M-2] + p[N-1]*B
		den = v
	else :
		den = p
	
	num =  np.array([1] + [0 for _ in range(N-1)])

	G_bp = abs(np.polyval(den,1j*Omega_p2)/(np.polyval(num,1j*Omega_p2)))

	return num, den, G_bp
