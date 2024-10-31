#class Animal:
   
#pass
   
#def __init__(self, animal_name, animal_species):
        #self.name = animal_name
        #self.species = animal_species


    #def make_sound(self):
        #print(f"{self.name}")
        #return 0
    
class Student:

    #class variable defined outside constructor and is shared
    #by both objects
    class_year = 2024
    num_students = 0 #keep track of number of students

    def __init__(self, name, age): #constructor
        self.name = name
        self.age = age
        Student.num_students +=1

#instances
student1 = Student("Spongebob", 30)
student2 = Student("Patrick", 35)


print(student1.name)
print(student1.age)
print(student1.class_year)
print(Student.num_students)

