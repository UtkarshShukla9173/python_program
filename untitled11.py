from array import *
a=[]
count=0
while(True):
    v=int(input())
    if v>0:
        a.append(v)
    else:
        break
#b=[1,2,3,4,5,6]
occ=0
v=int(input("enter the no")) #counting no manually with accumulator by increasing the value of count
for i in range(len(a)):
    if (a[i])==(v):
        count+=1
print(count)
print(a.count(v))  # counnting using in built functanality
#print(b)
a.insert(0, 10)
print(a)