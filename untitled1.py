class grt:
   
 
    def va():
        a=[10,20,30,40,50,55,60,70,80,90]
        val=int(input("enter the value to be searched"))
        cnt=0
        for i in a:
            if i == val:
                cnt=i
        if cnt>0:
            print("value found at index["+str(a.index(val))+"]")
        else:
            print("there is no such value in array")
    while(True):
        cs=input("do you want to search more elements y or n")
        if cs =='y':
            va()
        else:
            break