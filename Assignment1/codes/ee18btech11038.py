import soundfile as sf
import scipy as sp
from scipy import signal 
import matplotlib.pyplot as plt
import numpy as np
import math

import subprocess
import shlex

def subroutine_algo1(b, a, input_signal, store_x=None):
    N = len(b)
    M = len(a)


    if store_x==None: store_x = [0 for _ in range(N)]
    store_y = [0 for _ in range(M-1)]
    output_signal = [0 for _ in range(len(input_signal))]
    extra = [0 for _ in range(N)]
    for n in range(len(input_signal)):
        store_x[n%(N)] = input_signal[n]
        for k in range(N):
            output_signal[n] += b[k]*store_x[(n-k)%N]
        for m in range(1, M):
            output_signal[n] -= a[m]*store_y[(n-m)%(M-1)]
        output_signal[n] /= a[0]
        store_y[n%(M-1)] = output_signal[n]
    for i in range(N-1):
        n = len(input_signal) + i
        store_x[n%(N)] = 0
        for k in range(N):
            extra[i] += b[k]*store_x[(n-k)%N]
        for m in range(1, M):
            extra[i] -= a[m]*store_y[(n-m)%(M-1)]
        extra[i] /= a[0]
        store_y[n%(M-1)] = extra[i]
    return output_signal, extra



def algo1(b, a, input_signal):
    forward, exf= subroutine_algo1(b, a, input_signal)
    backward, exb = subroutine_algo1([1, 0.5], [1, 0.25], forward[::-1], exf[::-1])
    return backward[::-1]



def algo2(b, a, input_signal): 

	L = len(input_signal)
	z = np.exp(1j*2*np.pi*np.arange(L)/L)
	filt_poly_forward = np.polyval(b, z**(-1))/np.polyval(a, z**(-1))
	filt_poly_backward = np.polyval(b[::-1], z**(-1))/np.polyval(a[::-1], z**(-1))

	X = np.fft.fft(input_signal)
	V = np.multiply(filt_poly_forward,X)
	Y = np.multiply(filt_poly_backward, V)

	y = np.fft.ifft(Y).real
	return y



def norm(x, y):
    N = len(x)
    assert len(y)==N
    d = 0
    for i in range(N):
        d += (x[i] - y[i])**2
    return math.sqrt(d)




if __name__=='__main__':

	input_signal, fs = sf.read("../soundfiles/Sound_Noise.wav")
	sampl_freq = fs
	order = 4
	cutoff_freq = 4000.0
	Wn = 2*cutoff_freq/sampl_freq

	b, a = signal.butter(order, Wn, 'low')

	out0 = signal.filtfilt(b, a, input_signal)
	sf.write("../soundfiles/Sound_from_builtin_routine.wav", out0, fs)

	out1 = algo1(b, a, input_signal)
	sf.write("../soundfiles/Sound_from_algo1.wav", out1, fs)

	out2 = algo2(b, a, input_signal)
	sf.write("../soundfiles/Sound_from_algo2.wav", out2, fs)

	print("Norm b/w builtin and algo1 = ", norm(out0, out1))
	print("Norm b/w builtin and algo2 = ", norm(out0, out2))
	print("Norm b/w algo1 and algo2 = ", norm(out1, out2))

	plt.figure(1)
	plt.figure(figsize=(8,12))
	plt.subplot(3,1,1)
	plt.plot(out0,'r')
	plt.title('Output from builtin routine')
	plt.grid()

	plt.subplot(3,1,2)
	plt.plot(out1,'c')
	plt.title('Output from algorithm 1')
	plt.grid()

	plt.subplot(3,1,3)
	plt.plot(out2,'y')
	plt.title('Output from algorithm 2')
	plt.grid()

	plt.savefig('../figs/ee18btech11038_time.eps')

	plt.figure(2)
	plt.figure(figsize=(8,12))
	plt.subplot(3,1,1)
	plt.plot(np.abs(np.fft.fftshift(np.fft.fft(out0))),'r')
	plt.title('Output from builtin routine')
	plt.grid()

	plt.subplot(3,1,2)
	plt.plot(np.abs(np.fft.fftshift(np.fft.fft(out1))),'c')
	plt.title('Output from algorithm 1')
	plt.grid()

	plt.subplot(3,1,3)
	plt.plot(np.abs(np.fft.fftshift(np.fft.fft(out2))),'y')
	plt.title('Output from algorithm 2')
	plt.grid()

	plt.savefig('../figs/ee18btech11038_freq.eps')


