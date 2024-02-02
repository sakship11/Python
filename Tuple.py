#create tuple
tuple1=(1,2,3,"AIDS","PVPIT","CSE")
print(tuple1)

#Tuples are immutable

#Slicing of Tuple
print(tuple1[1:])

print(tuple1[::-1]) #Reverse Tuple

print(tuple1[3:5])  #sub tuple from insex 3 to 4

#Repetition
t2=('Python',)*3
print(t2)

#Length
t3=('Python','JAVA')
print(len(t3))

#Converting list to tuple
list1=[1,2,3]
print(tuple(list1))

#Delete Tuple
t4=(0,9,8,7,6)
del t4
print(t4)


