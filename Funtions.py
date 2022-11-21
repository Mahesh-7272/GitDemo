import self as self


class Car:

    def __init__(self, colour, body):
        self.clr=colour
        self.bd=body


    def carName(self):
        print("the colour is"+self.clr+"and body is"+self.bd)


p1=Car("yellow","SUV")
p1.carName()

