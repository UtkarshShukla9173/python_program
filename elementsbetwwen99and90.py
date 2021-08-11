a=[]
while(True):
    v=int(input())
    if v>0:
        a.append(v)
    else:
        break
cot=0
for i in a:
    if i>=90 and i<=99:
        cot+=1
print(cot)