n = int(input("Enter a number: "))
sum = 0
t = n

while t > 0:

   digit = t % 10
   sum += digit ** 3
   t //= 10

if n == sum:
   print(n,"is an Armstrong number")

else:
   print(n,"is not an Armstrong number")
