from array import *
a=[2,4,5,2,1,6,1,1,8,6,8,2,3,1,3,9]
count=0
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