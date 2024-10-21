#create  a list
favorite_fruits=["Mango","Orange","Pineapple","Avocado","Guava"]
print(favorite_fruits)

#add fruit
favorite_fruits.append("Strawberry")
print(favorite_fruits)

#remove the third fruit
favorite_fruits.pop(2)
print(favorite_fruits)

#sort in alphabetical order
favorite_fruits.sort()
print(favorite_fruits)

#Reverse
favorite_fruits.sort(reverse =True)
print(favorite_fruits)
favorite_fruits.reverse()
print(favorite_fruits)

#print length of the list
print(len(favorite_fruits))

#check if certain fruit is in the list
print("Strawberry" in favorite_fruits)

#for loop of the list
for  favorite_fruit in favorite_fruits:
    print(favorite_fruit)

#length for each fruit
fruit_length=[len(favorite_fruit)
for favorite_fruit in favorite_fruits:]
print(fruit_length)


