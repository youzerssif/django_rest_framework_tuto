class Poly():
    def __init__(self,*args):
        self.coeff1=args

    def coeff(self): 
        return list(self.coeff1)
    
    def evalue(self, x):
        return 1*x+2*x+x


poly = Poly(1,2,3)
print(poly.coeff())
print(poly.evalue(2))