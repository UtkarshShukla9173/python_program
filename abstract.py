from abc import ABC,abstractmethod

class computer(ABC):
  @abstractmethod
  def process(self):
    pass


class Laptop(computer):
  def process(self):
    print("its running")


class programmer:
  def work(self,comp):
    print("solving Bugs")

class whiteboard:
  def write(self):
    print("its writing")


#com = computer()
comp1= Laptop()
comp1.process()
comp2=whiteboard()
#com.process()
prog1= programmer()
prog1.work(comp1)
prog1.work(comp2)