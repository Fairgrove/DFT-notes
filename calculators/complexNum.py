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
                    self.phi = (3/4) math.pi
                else:
                    self.phi = 0

        def printNum(self):
            if Im < 0:
                print(str(self.Re) + ' - i' + str(self.Im))
            else:
                print(str(self.Re) + ' + i' + str(self.Im))
