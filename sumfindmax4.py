#a=[2,3,5,22,1,33,65,77,98,54,25]
a=[12,33,45,3,67,8,5]
sum=0
for i in range(4):
    sum+=max(a)
    a.remove(max(a))
print(sum)