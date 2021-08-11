'''for i in range(2,20):
    if i%2==0 or i%3==0:
        if i==2 or i==3:
            print(i,"is prime no")
        pass
    
    else:
        print(i, ' is prime no.')'''

for i in range(2,20):
    for x in range(2,i):
        if i%x==0:
            print(i,'equals',x,'*',i//x)
            break
    else:
        print(i ,'is prime no.')