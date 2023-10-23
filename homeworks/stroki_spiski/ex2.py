import random
TEMP = 10
def calculate(items: list):
   print(f"Maximum is: {max(items)}")
   print(f"Minimum is: {min(items)}")
   temps = 0
   sign_num = 0
   sign_num_2 = 0
   for item in items:
        if item < 0:
            sign_num += 1
        if item > 0:
            sign_num_2 += 1
        elif item == 0:
            temps += 1
   print(f"Count of nulls is: {temps}")
   print(f"Positive {sign_num_2}")
   print(f"Negative nums {sign_num}")
           

        

if __name__ == "__main__":
    list = []
    for i in range(10):
      list.append(random.randint(0, 10))
calculate(list)
   