a=[]
n=int(input("no of elements in array"))
for i in range(n):
    k=int(input("enter value at index ["+str(i)+"]"))
    a.append(k)
print(a)
count=0
for i in range(len(a)-1):
    for i in range(len(a)-1):
        if (a[i])==(a[i+1]):
            count+=1
print(a)