import numpy as np
from cheb import *
import math 
import matplotlib.pyplot as plt

#The low-pass Chebyschev design parameters
epsilon = 0.4
N = 4

#Analytically obtaining the roots of the Chebyschev polynomial
#in the left half of the complex plane

beta = ((np.sqrt(1+epsilon**2)+ 1)/epsilon)**(1/N)
r1 = (beta**2-1)/(2*beta)
r2 = (beta**2+1)/(2*beta)

#Obtaining the polynomial approximation for the low pass
#Chebyschev filter to obtain a stable filter
u = 1
for n in range(N//2):
	phi = np.pi/2 + (2*n+1)*np.pi/(2*N)
	v = [1,(-2*r1)*np.cos(phi),(r1**2)*((np.cos(phi))**2) + (r2**2)*((np.sin(phi))**2)]
	p = np.convolve(v,u)
	u = p

#The following was to verify that the roots obtained
#are correct
#roots(p)

p1 = epsilon**2*np.convolve(cheb(N),cheb(N)) + np.array([0 for _ in range(2*N)] + [1])
#r = roots(p1)


#Evaluating the gain of the stable lowpass filter
#The gain has to be 1/sqrt(1+epsilon^2) at Omega = 1
G = abs(np.polyval(p,1j))/np.sqrt(1+epsilon**2)

#Plotting the magnitude response of the stable filter
#and comparing with the desired response for the purpose
#of verification

Omega = np.linspace(0,2,201)
H_stable = abs(G/np.polyval(p,1j*Omega))
H_cheb = abs(np.sqrt(1/np.polyval(p1,1j*Omega)))
plt.plot(Omega,H_stable,'o', markerfacecolor='none', color = 'b', linewidth = 0.1)
plt.plot(Omega,H_cheb, linewidth = 0.5, color = 'r')

plt.xlabel('$\Omega$')
plt.ylabel('$|H_{a,LP}(j\Omega)|$')
plt.legend(['Design','Specification'])
plt.savefig('../../figs/specs.eps')

