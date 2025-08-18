class Animal:
    zoo_name = "Zoo"
    
    # 1. animal info
    def __init__(self, name, species, age, sound):
        self.name = name
        self.species = species
        self.age = age
        self.sound = sound
        
    # 2. printing animal's sound method
    def make_sound(self):
        print(f"{self.sound}")
        
    # 3. printing info method        
    def info(self):
        print(f"name: {self.name}, species: {self.species}, age: {self.age}, zoo: {self.zoo_name}")
        
    # 5. str method
    def __str__(self):
        return f"{self.species} named {self.name}, {self.age} years old, makes this sound {self.sound}"
    
# 4. bird class
class Bird(Animal):
    def __init__(self, name, species, age, sound, wing_span):
        super().__init__(name, species, age, sound)
        self.wing_span = wing_span
        
    # rewriting method
    def make_sound(self):
        print(f"{self.name} says: {self.sound}")
        
# testing  
# lion test
lion = Animal("Simba", "Shir", 5, "GRRRRR")

# bird test
eagle = Bird("bald eagle", "eagle", 3, "SCREECH", 2.5)

# using methods
lion.make_sound()
lion.info()
print(lion)

eagle.make_sound()
eagle.info()
print(eagle)