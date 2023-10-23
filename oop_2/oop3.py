class Pet:
    def __init__(self, name, age, color):
        self.name = name 
        self.age = age
        self.color = color
        
class Tiger(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age, color)
    def print_info(self):
        print(f"{self.name} {self.age} {self.color}")

class Crocodile(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age, color)
    def print_info(self):
        print(f"{self.name} {self.age} {self.color}")

class Kangaroo(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age, color)
    def print_info(self):
        print(f"{self.name} {self.age} {self.color}")

if "__main__" in __name__:
    tiger = Tiger("TIGER", 22, "red")
    tiger.print_info()
    croco = Crocodile("crocs", 1, "blue")
    croco.print_info()