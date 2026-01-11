# Step 1: Define the ZooAnimal class
class ZooAnimal:
    def __init__(self, name, species, sound):
        # Initialize the animal's name and species
        self.name = name
        self.species = species
        self.sound = sound

    def make_sound(self):
        # A method to make the animal "speak"
        print("{}, the {}, says : {}!".format(self.name, self.species, self.sound))
        
    def describe(self):
        # A method to describe the animal
        print("Animal: {} | Species: {}".format(self.name, self.species))

# Step 2: Create objects (instances) of ZooAnimal

# Create a few zoo animals
animal1 = ZooAnimal("Leo", "Lion", "Roar!")
animal2 = ZooAnimal("Ellie", "Elephant","Trumpet!")
animal3 = ZooAnimal("Zara", "Zebra","Don't eat me!")

# Call methods on the objects
animal1.make_sound()
animal1.describe()

animal2.make_sound()
animal2.describe()

animal3.make_sound()
animal3.describe()


