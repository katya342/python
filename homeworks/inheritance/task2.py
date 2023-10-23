class Ship:
    def __init__(self, name, model):
        self.name = name
        self.model = model

class Frigate(Ship):
    def __init__(self, name, model, size, speed, agility):
        super().__init__(name, model)
        self.size = size
        self.speed = speed
        self.agility = agility
    def print_info(self):
        print(f"Model is: {self.model} Size eq to {self.size} agility is {self.agility}")
class Destroyer(Ship):
    def __init__(self, name, model, protection, speed):
        super().__init__(name, model)
        self.protection = protection
        self.speed = speed
    def print_info(self):
        print(f"Name is {self.name} model is {self.model} speed is {self.speed}")
class Cruiser(Ship):
    def __init__(self, name, model, crew_size, capability):
        super().__init__(name, model)
        self.crew_size = crew_size
        self.capability = capability
    def print_info(self):
        print(f"Name is {self.name} crew size is {self.crew_size} capability is {self.capability}")

if __name__ == "__main__":
    cruiser = Cruiser("Cruiser", "AX400", 234, 33)
    cruiser.print_info()
    