from pet import Pet

import random #import random

# Set attributes for the pet

name = "Fluffy"
pet_type = "Dog"
age = 5
hunger = random.randint(0, 10) #Generate random hunger level from 0 to 10
energy = random.randint(0, 10) #Dog can have energy from 0 to 10
happiness = random.randint(0, 10) #Dog can have happiness from 0 to 10

# Create an instance of the Pet class

my_pet = Pet(name, pet_type, age, hunger, energy, happiness)

