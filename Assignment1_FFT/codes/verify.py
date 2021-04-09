import struct
import matplotlib.pyplot as plt
import numpy as np
#If using termux
import subprocess
import shlex



input=np.array([0, 9, 1, 1, 2, 0, 0, 1])
y=np.fft.fft(input)

plt.figure(figsize=(7,8))

plt.subplot(2,1,1)
plt.grid()
plt.title("Magnitude Spectrum")
plt.ylabel("|X(k)|")
plt.stem(np.abs(y),use_line_collection=True)


plt.subplot(2,1,2)
plt.grid()
plt.title("Phase Spectrum")
plt.xlabel("k")
plt.ylabel(r'$\angle{H(k)}$')
plt.stem(np.angle(y),use_line_collection=True)

plt.savefig('../figs/dftnumpy.pdf')
plt.savefig('../figs/dftnumpy.eps')
#If using termux
#subprocess.run(shlex.split("termux-open ../figs/dftnumpy.pdf"))
# plt.show()