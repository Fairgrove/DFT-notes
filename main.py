import matplotlib.pyplot as plt
import math
from random import randint

from scripts.DTFT import *
from scripts.plotters import *
from scripts.signal import *
from scripts.zTransform import *




signal = Signal(10000, 1)
signal.newSignal(11, 1)
# signal.newSignal(1, 1)
# signal.newSignal(33, 2)
# signal.newSignal(14, 1)

freqs = []
# for i in range(10):
#     freqs.append(randint(1, 100))
#     signal.newSignal(freqs[-1], 1)

zt = zTransform(signal, 11)
ft = DTFT(signal, range(1,100))

print(ft[1])
found = findFrqs(ft)
print(found)

plt.plot(ft[0], ft[1])
plt.show()
