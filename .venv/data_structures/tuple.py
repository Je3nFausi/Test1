#Example
my_tuple = (1, 2, 3)
print(my_tuple)

#Example2:Accessing elements by index
my_tuple=('apple', 'banana', 'cherry')
print(my_tuple[0])

#if you try making changes on a tuple you will get an error

#Example3: Tuple with mixed data types
mixed_tuple =(1, "hello", 3.14)
print(mixed_tuple)

#Example4:nested tuple
nested_tuple=(1, (2, 3), ('a','b'))
print(nested_tuple)

#slicing--getting a portion of the elements
animal_tuple =("Yellow anaconda", "Reptile", 30.5, 20)
sliced_tuple = animal_tuple[1:4]
print(sliced_tuple)   #has removed the first and last element



#Example7:Return the number of elements in animal_tuple
length_of_tuple = len (animal_tuple)
print( f"No. of attributes:  {length_of_tuple}")

#count the occurrence of the value false in animal_tupls
count_false = animal_tuple.count("Reptile")
print(count_false)

#assign each element in animal_tuple to individual variables
animal_tuple = ("Yellow anaconda", "Reptile", 30.5,20)
name, group, av_weight, av_lifespan = animal_tuple
print(f"Name: {name}")
print(f"Group: {group}")



