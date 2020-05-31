import numpy as np

class Weizsaecker:
    def __init__(self,Z,N):
        self.a_V = 15.67 # MeV
        self.a_A = 17.23 # MeV
        self.a_C = 0.714 # MeV
        self.a_S = 93.15 # MeV
        self.a_P = 11.2  # MeV
        self.Z = np.array(Z,dtype="float")
        self.N = np.array(N,dtype="float")
        self.A = np.add(Z , N)
        

    def volume_term(self):
        return self.a_V * self.A
        
    def surface_term(self):
        return - ( self.a_A * np.power(self.A,2/3) )
        
    def coulumb_term(self):
        return - ( self.a_C * self.Z * (self.Z - 1) * np.power(self.A,-1/3) )
        
    def asymmetry_term(self):
        return - ( self.a_S * (self.N - self.Z)**2/(4 * self.A) )

    def pairing_term(self):
        sign = []
        for i in range(self.Z.size):
            Z = self.Z[i] if self.Z.size > 1 else self.Z
            N = self.N[i] if self.N.size > 1 else self.N
            if(N % 2 > 0 and Z % 2 > 0):
                sign.append(-1.)
            elif(N % 2 == 0. and Z % 2 == 0.):
                sign.append(1.)
            else:
                sign.append(0.)
        return (np.array(sign) if len(sign) > 1 else sign[0]) * self.a_P * np.power(self.A,-1/2)

    def evaluate(self):
        result = 0.
        result += self.volume_term()
        result += self.surface_term()
        result += self.coulumb_term()
        result += self.asymmetry_term()
        result += self.pairing_term()
        return result/self.A
    

if(__name__ == "__main__"):
    test = Weizsaecker(4,4)
    print('gg',test.evaluate())
    test = Weizsaecker(5,4)
    print('ug',test.evaluate())
    test = Weizsaecker(4,5)
    print('gu',test.evaluate())
    test = Weizsaecker(5,5)
    print('uu',test.evaluate())


    arr_test = Weizsaecker([1,2,3,4,5,4,5],[1,2,3,4,4,5,5])
    print('arr_test',arr_test.evaluate())
