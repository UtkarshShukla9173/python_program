#import numpy as np
m=[]
for i in range(3):
    a=[]
    for j in range(3):
        j=int(input("enter the ["+str(i)+"] ["+str(j)+"]:"))
        a.append(j)
    m.append(a)
print(m)
n=[]
for i in range(3):
    b=[]
    for j in range(3):
        j=int(input("enter the ["+str(i)+"] ["+str(j)+ "]:"))
        b.append(j)
    n.append(b)
print(n)
result=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    for j in range(3):
        for k in range(3):
            result[i][j] += m[i][k]*n[k][j]
        print()
for i in range(3):
   for j in range(3):
        print(m[i][j],end=" ")
   print()
print("matrix 1")
for i in range(3):
   for j in range(3):
        print(n[i][j],end=" ")
   print()
print("matrix 2")

for i in range(3):
   for j in range(3):
        print(result[i][j],end=" ")
   print()
print("result matrix")
