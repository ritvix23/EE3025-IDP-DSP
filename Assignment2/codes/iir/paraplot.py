import numpy as np
import matplotlib.pyplot as plt
import cmath

# PLOTS OF THE LOWPASS CHEBYSCHEV FILTER OF ORDER N AND
# 0.3184 < epsilon < 0.6197

N = 4
epsilon = np.arange(0.35,0.61,0.05)
le = len(epsilon)
epsilon = epsilon.reshape(le,1)

omega = np.linspace(0,2,201)
omega = omega.reshape(len(omega),1)
lo = len(omega)
H = np.zeros((len(epsilon),len(omega)))


for i in range(len(epsilon)): 
	for j in range(len(omega)): H[i][j] =  (1/np.sqrt(1 + (epsilon[i]**2)*np.cosh(N*cmath.acosh(omega[j]))**2)).real
	plt.plot(omega,H[i,:], linewidth =0.1 )


leglist = ["$\epsilon$ = 0.35", "$\epsilon$ = 0.40","$\epsilon$ = 0.45","$\epsilon$ = 0.50","$\epsilon$ = 0.55","$\epsilon$ = 0.60"]
plt.xlabel("$\Omega$")
plt.ylabel("$|H_{a,LP}(j\Omega)|$")
plt.legend(leglist, loc ="upper right")
plt.savefig('../../figs/para_plot.eps')

