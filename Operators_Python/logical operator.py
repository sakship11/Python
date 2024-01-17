#logical and operator returns True if both the operands are True else it returns False.
a = 54
b = 22
if a > 0 and b > 0: 
    print("The numbers are greater than 0") 
else: 
    print("False")

#logical or returns True if either of the operands is True.
c=45
d=-21
if c > 0 or d > 0:
    print("Hello")
else:
    print("BYE")
    
# logical not operator works with a single boolean value.
#If the boolean value is True it returns False and vice-versa.
x=10
print(not(x > 3 and x <= 10))
