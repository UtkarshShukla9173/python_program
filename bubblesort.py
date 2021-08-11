a=[]
n=int(input("no of elements in array"))
for i in range(n):
    k=int(input("enter value at index ["+str(i)+"]"))
    a.append(k)
print(a)
temp=0
for i in range(n-1):
    for i in range(n-1):
        if (a[i])>(a[i+1]):
             temp=a[i]
             a[i]=a[i+1]
             a[i+1]=temp
print(a)