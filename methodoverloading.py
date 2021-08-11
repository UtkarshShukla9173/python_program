class students:
  def __init__(self,m1,m2):
    self.m1=m1
    self.m2=m2
  
  def sum(self,a=0,b=0,c=0):
    s=a+b+c
    ''' s=0
    if a!=0 and b!=0 and c!=0:
      s=a+b+c
    elif a!=0 and b!=0:
      s=a+b
    else:
      s=a'''
    
    return s
  
s1 =students(22,44)
print(s1.sum(5,9,6))
