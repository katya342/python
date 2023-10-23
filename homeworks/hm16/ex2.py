class Figure:
    def __init__(self, a):
        self.a = a
    def calculate(self) -> None:
        pass
class Rectangle(Figure):
    def __init__(self, a):
        self.a = a
    def __int__(self):
        return self.a * self.a
    def __str__(self) -> str:
        return f"Rectangle square is {self.__int__()}"
    
class RightTriangle(Figure):
    def __init__(self, a, b):
        super().__init__(a)
        self.b = b
    def __int__(self):
        return self.a * self.b
    def __str__(self):
        return f"RightTriangle square is {self.__int__()}"
    
class Trapezoid(Figure):
    def __init__(self, a, b, c):
        super().__init__(a)
        self.b = b
        self.c = c
    def __int__(self):
        return (self.a + self.b) * self.c / 2
    def __str__(self):
        return f"Trapezoid square is {self.__int__()}"
    
if __name__ == "__main__":
   figure_1 = Rectangle(2)
   print(figure_1)
   figure_2 = RightTriangle(2, 3)
   print(figure_2)