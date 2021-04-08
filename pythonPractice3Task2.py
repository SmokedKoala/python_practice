
class C32:
    
    # начальное состояние
    S0 = 'A'
 
    def wreck(self):
        if self.S0=='A':
            self.S0='B'
            return(0)
        elif self.S0=='B':
            return(3)
        elif self.S0=='E':
            self.S0='F'
            return(6)
        elif self.S0 == 'G':
            self.S0='E'
            return(9)
        else:
            return(None)    

    def chip(self):
        if self.S0=='C':
            self.S0='D'
            return(4)
        else:
            return(None)

    def carve(self):
        if self.S0=='A':
            self.S0='G'
            return(1)
        elif self.S0=='B':
            self.S0='C'
            return(2)
        elif self.S0=='D':
            self.S0='E'
            return(5)
        elif self.S0 == 'E':
            self.S0='C'
            return(7)
        elif self.S0 == 'F':
            self.S0='G'
            return(8)
        else:
            return(None)  
    
        
 

# o = C32()
# o.wreck()
# o.wreck()
# o.carve()
# o.chip()
# o.carve()
# o.wreck()
# o.carve()
# o.wreck()
# o.carve()
# o.chip()
# o.carve()
# o.carve()
# o.chip()
