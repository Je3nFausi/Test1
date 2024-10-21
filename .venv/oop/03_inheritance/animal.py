class Animal:
    def __init__(self, name):
        self.animal_name = name

    def make_sound(self):
        print(f" {self.animal_name} make sound")
        

class Dog(Animal):
    pass

class Cat(Animal):
    pass


dog = Dog("Simba")
dog.make_sound()


animal = Animal()