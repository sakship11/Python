
a = int(input("How many terms? "))
n1 = 0
n2=1
count = 0

if a <= 0:
   print("Please enter positive number!")

elif a == 1:
   print("Fiboaacci sequence upto",a,":")
   print(n1)
   
else:
   print("Fibonacci sequence:")
   while count < a:
       print(n1)
       temp = n1 + n2
      
       n1 = n2
       n2 = temp
       count += 1
