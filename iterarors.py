'''a=[7,8,9,5]
for i in a:
  print(i,"has index no:["+str(a.index(i))+"]")


it = iter(a) # iterraton has a function called next and we use it to print next values
print(it.__next__())
print(it.__next__())
print(next(it))'''

class Topten:
  def __init__(self):
    self.num =1
  
  def __iter__(self):
    return self

  def __next__(self):
    val = self.num
    self.num+=1

    return val
  
values = Topten()
for i in values:
  print(i)