def funn(*args,**kwargs):
    for i in kwargs.items():
        print(i,end=" ")
funn(a=10,b=20,c=30)