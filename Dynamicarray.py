def fun1(*args,**kwargs):
    for i in kwargs.items():
        print("value is",i)

a=[]

def rr():
     u=int(input("enter no of  entries"))
     for i in range(u):
        l=input("insert value y")
        fun1(l)
        a.append(l)


while True:
    print("do u want ro continue y or n")
    inp=input()
    
    if inp=='y':
        rr()
    else:
        print(a)
        break
        