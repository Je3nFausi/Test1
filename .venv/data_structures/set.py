#create an empty set called "unique numbers"
unique_numbers=set()

#create a ste with unique numbers
unique_numbers={1, 2, 3, 4, 5}

#create a set from a list
numbers ={1, 2, 3, 4, 5}
numbers_set = set(numbers)

#create set from a tuple
numbers_tuple=(1, 2, 3, 4, 5)
numbers_set=set(numbers_tuple)

#create a set from a string
numbers_string="12345"
numbers_set=set(numbers_string)
print(type(numbers_set))

#create a set from a range
numbers_range=range(1,6)

#check the type of the variable
type(numbers_set)

#add an element to the set
numbers_set.add(6)
print(numbers_set)

#remove an element
numbers_set.remove(6)
print(numbers_set)

#combine two sets
numbers_set2={6,7,8,9,10}
numbers_combined = numbers_set.union(numbers_set2)
print(numbers_combined)

#check if element is in the set
print(1 in numbers_set)

#clear the set
numbers_set.clear()
print(numbers_set)

#delete the set
del numbers_set
print(numbers_set)