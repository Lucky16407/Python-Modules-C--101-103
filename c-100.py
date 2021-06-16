class Element(object):
    def __init___ (self, number, symbol, mass):
        self.mass = mass
        self.number = number 
        self.symbol = symbol

sodium = Element( 11,"Na", 22)
iron = Element( 26,"Fe",52)
helium = Element(2,"He",4)

print(iron)
print(helium)