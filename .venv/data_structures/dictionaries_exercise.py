person={
    "Name":"John",
    "Age":25,
    "City":"New York"
}
print(person)

#add new value
person["job"]="Engineer"
print(person)

#update age value
person["Age"]=26
print(person)

#remove value
del person["City"]
print(person)

#check if key name exists in the dictionary
print("Name" in person)

#Iterate over the dictionary and print each key value
for key, value in person.items():
    print({key}, {value})

#create a dictionary from two lists
keys=["a", "b", "c"]
values=[1, 2, 3]
combine=dict(zip(keys, values))
print(combine)

#to merge two dictionaries
dict1={
    "a":1,
    "b":2
}
dict2={
    "c":3,
    "d":4
}
merged_dict={**dict1,**dict2}
print(merged_dict)

#dictionary that maps numbers from 1 to 5 to their squares
squares = {x:x**2 for x in range (1,6)}
print(squares)

#nested dictionary
people={
    "John":{
      "age":25,
    "job":"Engineer"
    },
    "Jane":{
        "Age":28,
        "job":"Data Scientist"
    }
}
print(people)