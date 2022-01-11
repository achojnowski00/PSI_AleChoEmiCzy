class Calculator:
    def __init__(self,a,b):
        self.a = a
        self.b=b
    def add(self):
        return self.a+self.b
    def difference(self):
        return self.a-self.b
    def multiply(self):
        return self.a*self.b
    def divide(self):
        return self.a/self.b


calc = Calculator(4,6)
print(calc.add())
print(calc.difference())
print(calc.multiply())
print(calc.divide())

class ScienceCalc(Calculator):
    def condemnation(self):
        return self.a*self.a,self.b*self.b

scalc = ScienceCalc(3,2)
print(scalc.add())
print(scalc.multiply())
print(scalc.condemnation())


        