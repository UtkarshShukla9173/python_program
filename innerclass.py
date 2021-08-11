class student:    #outer class
  def __init__(self,name,rolllno):
    self.name=name
    self.rollno=rolllno
    self.lap=self.laptop()
  
  def show(self):
    print(self.name,self.rollno)
    self.lap.show()

  class laptop: #inner class
    def __init__(self):
      self.brand='hp'
      self.cpu='i5'
      self.ram=8

    def show(self):
      print(self.brand,self.cpu,self.ram)
  


s1 = student('Navin',23)
s2 = student('jenny',32)
s1.show()


lap1=student.laptop()

lap1 =s1.lap
lap2= s2.lap
print(id(lap1))
print(id(lap2))