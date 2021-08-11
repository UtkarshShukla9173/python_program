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
for i in range(b):
    
    m= b.count(i)
    print(m)
    
    i=v
    b.pop(v)