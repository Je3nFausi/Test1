from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def eat(self):
        pass

class Dog(Animal):
    def make_sound(self):
        pass

    def eat(self):
        pass
    

dog = Dog()