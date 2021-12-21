def T(n):
   if (n<0):
   	return 0
   elif(n == 1):
   	return 1
   elif(n == 2):
   	return 2
   elif(n == 3):
   	return 4
   else:
     return T(n-1)+T(n-2)+T(n-3)
num = int(input ("Enter number :"))
print(T(num))

 



