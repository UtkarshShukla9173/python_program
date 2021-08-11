a=[2,3,4,5,2,4,5,6,1,8,7,6,5,2,5,3,99,4,5,8,2]
b=[]
for i in a:
    if i not in b:
        b.append(i)
        b.sort()
print(b)

a=[2,3,4,5,2,4,5,6,1,8,7,6,5,2,5,3,99,4,5,8,2]
set1=set()
for i in a:
    set1.add(i)
set1.update([11,22,'john','mohan','kritik',111,'kapil'])
print("this is set1",set1)
    







a=[1,2,3,4,5,6]
b=[5,6,7,8,9,1]
for i in a:
    for y in b:
        if i==y:
            print("the common element is",y)