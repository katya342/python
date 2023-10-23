
class Device:
    def __init__(self, name):
        self.name = name
        
class CoffeMachine(Device):
    def __init__(self, name, capacity):
        super().__init__(name)
        self.capacity = capacity
    def info(self) -> str:
        print(f"Coffe machine capacity is {self.capacity}")
class Blender(Device):
    def __init__(self, name, speed_level):
        super().__init__(name)
        self.speed_level = speed_level
    def print(self):
        print(f"Blenders speed eq to {self.speed_level}")
class MeatGrinder(Device):
    def __init__(self, name, type):
        super().__init__(name)
        self.type = type
if __name__ == "__main__":
    coffe = CoffeMachine("Bosh", 23)
    coffe.info()
    blend = Blender("Blender", 23)
    blend.print()
    
