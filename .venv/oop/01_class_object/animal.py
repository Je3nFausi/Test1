class Animal:
    pass
    def __init__(self, animal_name, animal_species):
        self.name = animal_name
        self.species = animal_species


    def make_sound(self):
        print(f"{self.name}")
        return 0