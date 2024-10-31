#class Animal:
    #def __init__(self, name):
#self.animal_name = name

   # def make_sound(self):
#print(f" {self.animal_name} make sound")
        

#class Dog(Animal):
   # pass

#class Cat(Animal):
   # pass


#dog = Dog("Simba")
#dog.make_sound()


#animal = Animal()

#inheritance-Allows a class to inherit attributes and methods from another class
#helps with code reusability and extensibility



class Animal:
    def __init__(self , name):#constructor
        self.name = name
        self.is_alive = True

    #all animals can do things, define them
    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):  #Dog will inherit from Animal
    pass

class Cat(Animal): # Cat will inherit from animal
    pass

class Mouse(Animal):  #Mouse will inherit from Animal multiple class Cat(Dog , Cow)
    pass

dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("Mickey")
        
print(dog.name)
print(dog.is_alive)
dog.eat()
dog.sleep()

print(cat.name)
print(cat.is_alive)
cat.eat()
cat.sleep()

print(mouse.name)
print(mouse.is_alive)
mouse.eat()
mouse.sleep()