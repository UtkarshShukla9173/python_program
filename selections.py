a=[23,22,45,67,89,1,2,56,4,7]
#temp=0
for i in range(len(a)):
  temp=i
  for j in range(i+1,len(a)):
    if a[i]>a[j]:
      temp=j
      a[i],a[temp]=a[temp],a[i]
      #a[i]=a[j]
      #a[temp]=a[i]
print("sorted array")
for i in range(len(a)):
  print(a[i],end=" ")


