
# %THIS PROGRAM FINDS THE FIR COEFFICIENTS FOR A BANDPASS FILTER USING THE
# %KAISER WINDOW AND THE DESIGN SPECIFICATIONS


import numpy
import matplotlib.pyplot as plt
from math import pi
from math import ceil
from numpy import log10
from numpy import sin, cos

# %Filter number
L = 114

# %Sampling freqency (kHz)
Fs = 48


# %Constant used to get the normalized digital freqencies
const = 2*pi/Fs


# %The permissible filter amplitude deviation from unity
delta = 0.15

# %Bandpass filter specifications (kHz)

# %Passband F_p2 < F_p1
F_p1 = 3 + 0.6*(L-107)
F_p2 = 3 + 0.6*(L-109)

# %Transition band
delF = 0.3

# %Stopband F_s2 < F_p21 F_p1 < F_s1
F_s1 = F_p1 + 0.3
F_s2 = F_p2 - 0.3



# %Normalized digital filter specifications (radians/sec)
omega_p1 = const*F_p1
omega_p2 = const*F_p2

omega_c = (omega_p1+omega_p2)/2
omega_l = (omega_p1-omega_p2)/2

omega_s1 = const*F_s1
omega_s2 = const*F_s2
delomega = 2*pi*delF/Fs

# %The Kaiser window design
A = -20*log10(delta)

N = 100
n = numpy.linspace(-N, N, 2*N+1).reshape(2*N+1, 1)
n[100] = 0.0000000001



hlp = sin(n*omega_l)/(n*pi)
hlp[N] = omega_l/pi
hbp = 2*hlp*cos(n*omega_c)



omega = numpy.linspace(-numpy.pi/2,numpy.pi/2,201)

Hlp = numpy.abs(numpy.polyval(hlp,numpy.exp(1j*omega)**(-1)))
plt.figure(1)
plt.plot(omega/numpy.pi,Hlp, linewidth = 0.1, color = 'b')
plt.xlabel('$\omega/\pi$')
plt.ylabel('$|H_{lp}(\omega)|$')
plt.savefig('../../figs/fir-lowpass.eps')


Hbp = numpy.abs(numpy.polyval(hbp, numpy.exp(1j*omega)**(-1)))
plt.figure(2)
plt.plot(omega/numpy.pi,Hbp, linewidth = 0.1, color = 'b')
plt.xlabel('$\omega/\pi$')
plt.ylabel('$|H_{bp}(\omega)|$')
plt.savefig('../../figs/fir-bandpass.eps')


fir_coeff = hbp
numpy.savetxt("fir_coeff.dat",fir_coeff)