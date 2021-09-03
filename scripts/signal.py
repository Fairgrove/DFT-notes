import math

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
