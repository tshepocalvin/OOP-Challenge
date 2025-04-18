class Pet:
    def __init__(self, name,pet_type, age, hunger, energy, happiness):
        self.name = name
        self.pet_type = pet_type
        self.age = age
        self.hunger = hunger
        self.energy = energy
        self.happiness = happiness



def get_status(self):
        print(f"🌟 {self.name}'s Status 🌟")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")
        print("-" * 25)