list1=["one",2,"three"]  #create list and print it
type(list1)
print(list1)

list1.insert(2,3)  #insert element at specific position
print(list1)

list1.append("PVPIT") #insert element at the end
print(list1)

list1.extend(["CSE","AIDS"])  #multiple elements are added by extend()
print(list1)

list1.reverse()   #Reverse the list
print(list1)

list1.remove(3) #Remove the specific element
print(list1)

list1.pop()     #removes the element at the end
print(list1)

print(list1[1:])  #Slice- get the sublist from index 1

print(list1[::-1])  #Reverse list using slice method

print(list1[2:4])   #get sublist from index 2 to 3
