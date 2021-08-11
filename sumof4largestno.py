a=[12,33,45,3,67,8,5]
a.sort()
print(a)
b=[]
sum=0
for i in range(1,5):
    c=(a[(len(a)-i)])
    print(c)
    b.append(c)
    #a.remove(c)
print(a)
print(b)

for i in b:
    sum+=i
print(sum)