import matplotlib.pyplot as plt
import math
from random import randint

# from scripts.DTFT import *
# from scripts.plotters import *
# from scripts.signal import *
# from scripts.zTransform import *

from scripts import *

signal = Signal(10000, 1)
# signal.newSignal(11, 1)
# signal.newSignal(1, 1)
# signal.newSignal(33, 2)
# signal.newSignal(14, 1)

for i in range(10):
    signal.randSignal(1,40)

zt = zTransform(signal, 1)
ft = DTFT(signal, range(0,40))

fig, axs = plt.subplots(3)
axs[0].set_ylabel('Amplitude')
axs[0].set_xlabel('Samples')
axs[0].set_title('Complex plane')
axs[0].plot(signal.signal)

axs[1].set_ylabel('Im(z)')
axs[1].set_xlabel('Re(z)')
#axs[1].set_xlim(-3,3)
#axs[1].set_ylim(-3,3)
axs[1].set_title('Z-plane')
axs[1].plot(zt[0], zt[1])

axs[2].set_title('F-plane, found: ' + str(len(findFrqs(ft))) + '  ' + str(len(signal.frequencies)) + ' created\n' + str(signal.frequencies))
axs[2].set_ylabel('Amplitude/2')
axs[2].set_xlabel('Frequence')
axs[2].bar(ft[0], ft[1])

fig.tight_layout() #prevent labels overlapping
plt.show()
