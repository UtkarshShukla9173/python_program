a=[]
while(True):
    v=int(input())
    if v>0:
        a.append(v)
    else:
        break
b=[]
print(a)
for i in a:
    if i <10:
        b.append(i)
        
print(b)
count=0  
for i in range(len(a)):
    if (a[i])in b[i]:
        count+=1
print(count)
