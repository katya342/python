class Human:
    def __init__(self, name):
        self.name = name
        
    
class Builder(Human):   
    def __init__(self, name, specialization):
        super().__init__(name, specialization)

    def __str__(self) -> str:
        return f"Строитель:  {self.name}"
    def building(self):
        return f"{self.name} {self}"

class Sailor(Human):
    def __init__(self, name):
        super().__init__(name)
    def __str__(self) -> str:
        return f"Sailor man:  {self.name}"
    

class Pilot(Human):
    def __init__(self, name):
        super().__init__(name)
    def __str__(self) -> str:
        return f"Pilot man: {self.name}"

if "__main__" in __name__:
    builder = Builder("Builder_1")
    print(builder)
    builder.building()
    
   
    