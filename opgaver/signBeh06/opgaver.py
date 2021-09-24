import math

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
