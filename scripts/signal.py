import math
from random import randint

class System:
    signals = []
    inputSignal = []
    frequencies = []
    outputSignal = []

    def __init__(self, fs, t, h):
        self.fs = fs #sample rate
        self.t = t #sample time
        self.h = h #impulse response


    def randSignal(self, min, max):
        #if all frequencies in range are in use, do nothing
        #find a resolution for cheking
        #check frq spectrum funcion

        f = randint(min, max)

        #keep generating frequencies until one that isn't used is found
        while self.checkFrequency(f):
            f = randint(min, max)

        self.newSignal(f, 1)

    def checkFrequency(self, f):
        """
        returns false if given frequency is not in use
        i.e true if frequency is in use
        """

        if len(self.frequencies) != 0:
            return False

        for ii in self.frequencies:
            if f == ii:
                return True
        return False

    def newSignal(self, f, A):
        new = []
        self.signals.append(new)
        self.frequencies.append(f)

        for n in range(1, math.ceil(self.t*self.fs+1)):
            y = A + A * math.sin((n/self.fs)*(f*2*math.pi))
            self.signals[-1].append(y)

            if len(self.signals) > 1:
                self.inputSignal[n-1] += y
            else:
                self.inputSignal.append(y)

        #[sys.inputSignal,range(len(sys.inputSignal))]
        self.calcOutputSignal()

    def calcOutputSignal(self):
        #convolve inputSignal with impulse response
        #this is done by mirroring the impulse response about the origin
        #each sample in the inputSignal is added
        #    with every sample of the impulse response

        hMirror = [[],[]]
        for n in range(len(self.h[0])):
            hMirror[0].append(self.h[0][-1-n])
            hMirror[1].append(self.h[1][-1-n])

        #convolution (x[n] * h[n])

def convolve(x1, x2):
    result = [[], []]

    high = x2[0][-1]
    low = x2[0][0]
    extend = high + low
    if low < 0:
        extend += -2*low

    for i in range(len(x1[0]) +extend):
        result[0].append(i)
        result[1].append(0)

    print(low, high)
    print(result[0])
    print(len(result[0]))

    for n in x1[0]:
        for k in x2[0]:
            if low < 0:
                mark = n + k - low
            else:
                mark = n + k

            result[1][mark] += x1[1][n] * x2[1][k]

    print(len(x1[1]), x1[1])
    print(len(result[1]),result[1])

    return result


h = [[0,10,20,30,40,50],[2, 1.6, 1.3, 1, 0.6, 0.3]]
sys = System(10000, 1, h)
sys.newSignal(10,1)

a = [range(len(sys.inputSignal)), sys.inputSignal]

b = convolve(a, h)

import matplotlib.pyplot as plt
fig, axs = plt.subplots(2)
axs[0].set_title('input')
axs[0].plot(a[0], a[1])

axs[1].set_title('output')
axs[1].plot(b[0], b[1])
