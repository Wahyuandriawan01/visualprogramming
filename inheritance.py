class manusia:
  def __init__(self, pria, wanita):
    self.pria = pria
    self.wanita = wanita
 
  def printname(self):
    print(self.pria, 'and' ,self.wanita)

class gender(manusia):
  pass

gender1 = gender("Wahyu andriawan", "Dhea")
gender1.printname()
gender1 = gender("Ananda", "Selvi")
gender1.printname()
