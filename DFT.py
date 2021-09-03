import matplotlib.pyplot as plt
import math
from random import randint

class Signal:
    signals = []
    signal = []

    def __init__(self, fs, t):
        self.fs = fs #sample rate
        self.t = t #sample time

    def newSignal(self, f, A):
        new = []
        self.signals.append(new)

        for n in range(1, math.ceil(self.t*self.fs+1)):
            y = A + A * math.sin((n/self.fs)*(f*2*math.pi))
            self.signals[-1].append(y)

            if len(self.signals) > 1:
                self.signal[n-1] += y
            else:
                self.signal.append(y)

    def zTransform(self, f):
        transform = [[],[]]

        for i in range(len(Signal.signal)):
            #phi = 2*math.pi*(1/f)*i
            phi = i/(self.fs/f) * 2 * math.pi
            transform[0].append(self.signal[i] * math.cos(phi))
            transform[1].append(self.signal[i] * -math.sin(phi))

        return transform

    def center(self, f):
        output = 0

        transform = self.zTransform(f)

        for y in transform[1]:
            output += y

        return output/len(transform)



signal = Signal(10000, 2)
freqs = []
for i in range(20):
    freqs.append(randint(1, 100))
    signal.newSignal(freqs[-1], randint(1, 3))
# signal.newSignal(11, 1)
# signal.newSignal(1, 3)
# signal.newSignal(33, 1)
# signal.newSignal(14, 1.1)

centers = [[],[]]
for ioi in range(1, 50):
    centers[0].append(ioi)
    centers[1].append(signal.center(ioi))

fig, axs = plt.subplots(3)

axs[0].set_ylabel('Amplitude')
axs[0].set_xlabel('Samples')
axs[0].set_title('Complex plane')
axs[0].plot(signal.signal)

axs[1].set_ylabel('Im(z)')
axs[1].set_xlabel('Re(z)')
#axs[1].set_xlim(-3,3)
#axs[1].set_ylim(-3,3)
axs[1].set_title('Z-plane  ' + str(signal.center(11)))
axs[1].plot(signal.zTransform(11)[0], signal.zTransform(11)[1])

axs[2].set_title('centers')
axs[2].plot(centers[1])

fig.tight_layout(pad=1)

plt.show()
