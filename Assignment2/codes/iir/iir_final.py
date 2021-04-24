import numpy as np
import matplotlib.pyplot as plt
from para import *
from lp_stable_cheb import *
from lpbp import *
from bilin import *

epsilon = 0.4
[p, G_lp] = lp_stable_cheb(epsilon, N)

Omega_L = np.linspace(-2,2,401)
H_analog_lp = G_lp*abs(1/np.polyval(p,1j*Omega_L))
plt.figure(1)
plt.plot(Omega_L,H_analog_lp, linewidth = 0.1, color = 'b');
plt.xlabel('$\Omega$')
plt.ylabel('$|H_{a,LP}(j\Omega)|$')
plt.savefig('../../figs/iir-lowpass-analog.eps')


# The analog bandpass filter
[num,den,G_bp] = lpbp(p,Omega_0,B,Omega_p1)

Omega = np.linspace(-0.65,0.65,131)
H_analog_bp = G_bp*abs(np.polyval(num,1j*Omega)/np.polyval(den,1j*Omega))
plt.figure(2)
plt.plot(Omega,H_analog_bp, linewidth = 0.1, color = 'b');
plt.xlabel('$\Omega$')
plt.ylabel('$|H_{a,BP}(j\Omega)|$')
plt.savefig('../../figs/iir-bandpass-analog.eps')


# The digital bandpass filter
[dignum,digden,G] = bilin(den,omega_p1)

omega = np.linspace(-2*np.pi/5,2*np.pi/5,801)
H_dig_bp = G*abs(np.polyval(dignum,np.exp(-1j*omega))/np.polyval(digden,np.exp(-1j*omega)))
plt.figure(3)
plt.plot(omega/np.pi,H_dig_bp, linewidth = 0.1, color = 'b')
plt.xlabel('$\omega/\pi$')
plt.ylabel('$|H_{d,BP}(\omega)|$')
plt.savefig('../../figs/iir-bandpass-dig.eps')

iir_num = G*dignum
iir_den = digden

np.savetxt("iir_num.dat",iir_num)
np.savetxt("iir_den.dat",iir_den)
np.savetxt("dignum.dat",dignum)
np.savetxt("digden.dat",digden)
np.savetxt("G.dat",np.array([G]))

#plt.show()