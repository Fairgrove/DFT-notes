import math
from random import randint

class Signal:
    signals = []
    signal = []
    frequencies = []

    def __init__(self, fs, t):
        self.fs = fs #sample rate
        self.t = t #sample time


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
                self.signal[n-1] += y
            else:
                self.signal.append(y)
