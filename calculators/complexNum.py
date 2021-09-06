import math
import matplotlib.pyplot as plt

class ComplexNum():
        def __init__(self, Re, Im):
            #Rectangular form
            self.Re = Re #real part
            self.Im = Im #imaginary part

            #Polar Form phi is also called the argument of z
            self.r = math.sqrt((Re**2)+(Im**2))
            if self.Re != 0:
                self.phi = math.atan(Im/Re)
            else:
                if self.Im > 0:
                    self.phi = math.pi/2
                elif self.Im < 0:
                    self.phi = (3/4) * math.pi
                else:
                    self.phi = 0

        def printNum(self):
            if self.Im < 0:
                print(str(self.Re) + ' - i' + str(-1 * self.Im))
            else:
                print(str(self.Re) + ' + i' + str(self.Im))

        def printPolar(self):
            print(self.r, '(cos(', self.phi, ') + i sin(', self.phi, '))')

def plotNums(*argv):
    for z in argv:
        print(z.Re, z.Im)
        plt.plot(z.Re, z.Im, 'o')
    plt.ylabel('Im')
    plt.xlabel('Re')
    plt.style.use('ggplot')
    #plt.hlines(y=0, color='k')
    #plt.grid(True, which='both')
    plt.show()


def complexAdd(z1, z2):
    a = z1.Re + z2.Re
    b = z1.Im + z2.Im

    return ComplexNum(a, b)

def complexSub(z1, z2):
    a = z1.Re - z2.Re
    b = z1.Im - z2.Im

    return ComplexNum(a, b)

def complexMul(z1, z2):
    a = z1.Re * z1.Re - z1.Im * z2.Im
    b = z1.Im * z2.Re + z1.Re * z2.Im

    return ComplexNum(a, b)

def complexDiv(z1, z2):
    a = (z1.Re * z1.Re - z1.Im * z2.Im) / (z2.Re + z2.Im)
    b = (z1.Im * z2.Re + z1.Re * z2.Im) / (z2.Re + z2.Im)

    return ComplexNum(a, b)


z1 = ComplexNum(2, 7)
z2 = ComplexNum(-2, 11)
r = complexSub(z1,z2)
# r.printNum()
# r.printPolar()


plotNums(z1,z2,r)
