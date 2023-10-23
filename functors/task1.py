
class Addition:
    
    def __call__(self, x, y):
        return x + y




if __name__ == "__main__":
   addition = Addition()
   rezult = addition(5, 3)
   print(rezult)