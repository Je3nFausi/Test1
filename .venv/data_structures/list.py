#create an empty list
animals=[]
print(type(animals)) #shows that its a list

#create a list defined by square brackets--a list
animals=["Lion", "Elephant", "Dolphin"]
print(animals)

#create a list from a tuple using the list constructor
birds=list(("Eagle", "Penguin", "Parrot"))  #when using curved brackets its a tuple
print(birds)

#we can join two lists
combined_list=animals +birds
print(combined_list)

#Generate a list of values 0 to 5
range_list =list(range(0,5))
print(range_list)

#create a copy--helps retain data when you lose the original data set
animals_copy = animals.copy()

#nested list
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list)   #print(nested_list[1]) access specific list
access_nested=nested_list[2]

#modification--changing an element
#modify the 1st element of the animals list
animals[0]="Tiger"
print(animals)

append_animal = animals.append("Giraffe")#Adding Giraffe to the List
print(animals)

extend_animal = animals.extend(["Zebra", "Kangaroo"])  #adding more than 1 element
print(animals)

insert_animal = animals.insert(2, "Cheetah")   #To insert at a specific position of the list
print(animals)

remove_animal = animals.remove("Elephant") #To remove specific
print(animals)

#clear_animal=animals.clear()  #To clear the whole list
#print(animals)

pop_animal = animals.pop(2)  #also removes specified item
print(animals)

#order
#reverse the order of animals in the list
animals.reverse()
print(animals)

#sort list in ascending order
animals.sort()
print(animals)

#descending order
animals.sort(reverse=True)
print(animals)

