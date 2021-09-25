import math
import matplotlib.pyplot as plt

def readFile(name):
    file = open(name)
    content = file.read()
    return content.splitlines()

R = 1
C = 1
fs = 8

#therefore

T = 1/fs

print('\nOPGAVE 1\n----------')
def DTIR(n):
    return T/(R*C) * math.e ** -((n*T)/(R*C))

for i in range(1,6):
    print('h[', i, '] =', T/(R*C), 'e^ -(', i, '*', ((T)/(R*C)), ') =', DTIR(i))

print('\nOPGAVE 2\n----------')

def convolutionSum1():
    y = []
    for n in range(200):  # amount of samples in time series
        sum = 0
        for m in range(100): # amount of samples in impulse response
            h = DTIR(m)

            #calculating u[n-m]
            #in this input x is u[n]... so in conv sum it is u[n-m]
            if (n-m) >= 0:
                u = 1
            elif (n-m) < 0:
                u = 0

            sum += h * u
        y.append(sum)
    return y

y = convolutionSum1()
plt.plot(y)
plt.title(y[-1])
plt.show()
