class Pet():
     def __init__(self, name, breed):
        self.name = name
        self.breed = breed

     def sound(self) -> None:
         pass

     def show(self):
         print(f"Breed is {self.name}")

     def type(self):
         print(f"Breed is {self.breed}")
        

class Cat(Pet):
    def __init__(self, name:str):
        super().__init__(name, "Cat")

    def sound(self):
        print("meow")

class Dog(Pet):
    def __init__(self, name: str):
        super().__init__(name, "Dog")

class Legs(Pet):
    def __str__(self, count) -> str:
        print(f"Legs are {count}")
        


if __name__ == "__main__":
    pets_1 = Pet("cat", "catss")
    pets_1.show()
    pets_1.sound()
    pets_1.type()
   


        