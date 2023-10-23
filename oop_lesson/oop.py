class Shape:  

    def area(self):
        print("Метод не реализован")

class Rectangle(Shape):
     def __init__(self, a, b):
        self.a = a
        self.b = b
     def area(self):
         return self.a * self.b
     
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3,14 * self.radius * self.radius
        

if __name__ == "__main__":
   shape = Shape()
   print(shape.area())
   rectangle = Rectangle(4, 5)
   print(rectangle.area())

   circle = Circle(3)
   print(circle.area())