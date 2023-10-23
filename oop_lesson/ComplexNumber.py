class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __add__(self, other):
        real_sum = self.a + other.a
        imag_sum = self.b + other.b
        return ComplexNumber(real_sum, imag_sum)

    def __sub__(self, other):
        return self.a - other.a, self.b - other.b

    def __str__(self) -> str:
        return f"{self.a} + {self.b}i"
if __name__ == "__main__":
   c1 = ComplexNumber(1, 2)
   c2 = ComplexNumber(3, 4)
   rezult_add = c1 + c2
   #rezult_sub = c1 - c2
   print(rezult_add)

