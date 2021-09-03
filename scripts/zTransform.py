import math

def zTransform(signal, f):
    transform = [[],[]]

    for i in range(len(signal.signal)):
        phi = i/(signal.fs/f) * 2 * math.pi
        transform[0].append(signal.signal[i] * math.cos(phi))
        transform[1].append(signal.signal[i] * math.sin(phi))

    return transform
