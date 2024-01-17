#Creating array
from array import *
arr= array('b',[1,2,3,4,5])
type(arr)
print(arr)
print("======================================")

#Travesring using for loop
from array import *
arr= array('d',[1,2,3,4,5])
for x in arr:
    print(x)
print("======================================")

#Insert an element
from array import *
arr= array('b',[1,2,3,4,5])
arr.insert(2,9)
for x in arr:
    print(x)
print("======================================")

#Delete an element
from array import *
arr= array('i',[1,2,3,4,5])
arr.remove(2)  #Delete specific element
print(arr)
print("======================================")

from array import *
arr= array('i',[1,2,3,4,5])
arr.pop()  #Delete last element
print(arr)
print("======================================")

#Updatation
from array import *
arr= array('i',[1,2,3,4,5])
arr[2]=8  #Delete last element
print(arr)
print("======================================")

#Searching
from array import *
arr= array('i',[1,2,3,4,5])
x=arr.index(3)
print(x)









