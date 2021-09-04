from scripts.zTransform import *

def DTFT(signal, spectrum):
    """
    takes a z-transformed signal and fourier transforms it...
    """

    centers = [[],[]]
    for f in spectrum:
        centers[0].append(f)
        centers[1].append(0)
        if f != 0:
            transform = zTransform(signal, f)
            #calc average of all samples in transform
            for y in transform[1]:
                centers[1][-1] += y
            centers[1][-1] = centers[1][-1] / len(transform[1])

    return centers

def findFrqs(signal):
    """
    identifies the present frequencies in a fourier transformed signal
    """
    frqs = []

    for i in range(len(signal[0])):
        if signal[1][i] > 0.1:
            frqs.append(signal[0][i])

    return frqs
