from Inhertance import Calculator


class ChilImpl(Calculator):
  num2=200
  def __init__(self):
    Calculator.__init__(self, 8, 8)

  def getCompletedData(self):
    return self.num2+self.Summation()+self.num

demo=ChilImpl()
print(demo.getCompletedData())



