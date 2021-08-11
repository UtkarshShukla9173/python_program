a=[]
while(True):
    v=int(input())
    if v>0:
        a.append(v)
    else:
        break
b=[]

for i in a:
    if i <10:
        b.append(i)
print(b)
h=set()
for i in range(0,len(b)):
    h.add(b[i])
print(h)
j=[]
for i in range(0,len(b)):
    v=b.count(b[i])
    if b[i]!=b[i-1]:
        print(" ["+str(b[i])+"] appeared ",v,"no of times")
        j.append(v)
avg=sum(j)//len(h)
print(avg)