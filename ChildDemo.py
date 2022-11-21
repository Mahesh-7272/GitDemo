from OopsDemo import addition


class Abc(addition):
    num2=200

    def __init__(self):
        addition.__init__(self,2,10)

    def getCompletedData(self):
        return self.num2+self.num+self.summation()


obj2=Abc()
print(obj2.getCompletedData())