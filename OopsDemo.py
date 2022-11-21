class addition:

    num = 100
    def __init__(self,a,b):
        self.firstnumber=a
        self.secondnumber=b

        print("i called automatically when object is created")

    def getData(self):
        print("i am now executing as a method in class")
    def summation(self):
        print(self.firstnumber+self.secondnumber+self.num)

obj=addition(2,3)
obj.getData()
obj.summation()