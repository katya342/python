class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        if type(self.n) == str and type(other.n) == str:
            return self.n + other.n
       
        elif type(self.n) == int and type(other.n) == int:
            return self.n + other.n
        elif type(self.n) == str and type(other.n) == int:
            return self.n + str(other.n)
    
    def __sub__(self, other):
        if type(self.n) == str and type(other.n) == str:
            return self.n - other.n
       
        elif type(self.n) == int and type(other.n) == int:
            return self.n - other.n  
    
    def __div__(self, other):
        if type(self.n) == str and type(other.n) == str:
            return self.n / other.n
       
        elif type(self.n) == int and type(other.n) == int:
            return self.n / other.n
    
    def __mul__(self, other):
        if type(self.n) == str and type(other.n) == str:
            return self.n * other.n
       
        elif type(self.n) == int and type(other.n) == int:
            return self.n * other.n

if __name__ == "__main__":
    num_1 = Number(23)
    num_2 = Number(2)
    num_3 = Number("HELLOWORLD")
    num_4 = Number(10)
    print(num_1 * num_2)
    print(num_3 + num_4)
    