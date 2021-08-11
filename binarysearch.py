a=[]
n=int(input("no of elements in array"))
for i in range(n):
    k=int(input("enter value at index ["+str(i)+"]"))
    a.append(k)
print(a)


lt=1
rt=n
md=(lt+rt)//2

val=int(input("enter value "))
for i in a:

    if val > (a[md]):
        lt=md+1
        # print("lt updated")
    else:
        if val < (a[md]):
            rt=md-1
          #  print("rt updated")
        else:
            print("value found at location",md)
            
            break
    md=(lt+rt)//2
print("middle index:",md)
print("value at middle index:",a[md])
    