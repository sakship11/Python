#create set
set1={1,2,3,4,5,6}
print(set1)

#Adding elements
set1.add("PVPIT")
print(set1)

#update set
set1.update([10,11])  #Adding multiple elements
print(set1)

#Removing item from set
set1.remove(2)  
print(set1)

set1.discard(4)
print(set1)

set1.pop()
print(set1)

set2={1,2,3,4,5}
set3={3,4}
result=set2.union(set3)
print(result)

result2=set2.intersection(set3)
print(result2)

result3=set2.difference(set3)
print(result3)
