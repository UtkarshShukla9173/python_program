a=input("enter a string")
b=[]
for i in a:
    b.append(i)         #declared araay and appending all value of a in it to apply in built functanality of array like pop remove etc.
print(b)
v=input("enetr the alphabet oyu want to remove from string")
b.remove(v)
b.reverse()
for i in b:
    print(i,end=' ')