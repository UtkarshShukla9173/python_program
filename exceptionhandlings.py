a=5
b=2
try:
  print("resource open")
  print(a/b)
  k = int(input("enter a value"))
except ValueError as e:
  print("Invalid input",e)
except Exception as e:
  print("hey you cannot devide no. by 0", e )

finally:
  print("resource closed")
