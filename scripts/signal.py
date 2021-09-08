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
    result = [[],[]]

    for nx1 in x1[0]:
        for nx2 in x2[0]:
            n = nx1 + nx2


                


h = [[0,1],[2,1]]
sys = System(10000, 1, h)
sys.newSignal(10,1)

a = [sys.inputSignal,range(len(sys.inputSignal))]
print(len(a[0]), '  ', len(a[1]))
print(a[0])
print(a[1][0])
