class A:
  def __init__(self):
    print("in  A Init ")
  def feature1(self):
    print("feature1_A is working")
  def feature2(self):
    print("feature2 is working")

class B:
  def __init__(self):
    
    print("In B Init")
  def feature1 (self):
    print("feature1_B is working")
  def feature4 (self):
    print("feature4 is working")  

class C(A,B):
  def __init__(self):
    super().__init__()
    print("In C Init")
  def feat(self):
    super().feature2()

    


a1= C()
a1.feature1()
