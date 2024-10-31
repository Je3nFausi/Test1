#from abc import ABC, abstractmethod

#class Animal(ABC):

   # @abstractmethod
    #def make_sound(self):
     #   pass

    #@abstractmethod
    #def eat(self):
     #   pass

#class Dog(Animal):
 #   def make_sound(self):
  #      pass

   # def eat(self):
    #    pass
    

#dog = Dog()

#abstract class- A class that cannot be instantiated on its own; Meant to be subclassed
#can contain abstract methods, which are declared but have no implementation
#benefits:
#1.Prevents instantiation of the class itself
#2.Requires children to use inherited abstract methods

#we need to import abc

from abc import ABC, abstractmethod
class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    #create children to inherit

class Car(Vehicle):
    def go(self):
        print("You drive the car")

    def stop(self):
        print("You stop the car")

car = Car()
car.go()
car.stop()

class Motorcycle(Vehicle):
    def go(self):
        print("You ride the motorcycle")
    def stop(self):
        print("You stop the motorcycle")

motorcycle = Motorcycle()
motorcycle.go()
motorcycle.stop()
