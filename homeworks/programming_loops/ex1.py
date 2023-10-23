def calculate(num_1, num_2):
    for i in range(num_1, num_2):
        if primary_number(i) == True:
            print(f"Primary number is {i}")

def primary_number(number) -> bool:
     if number <= 1:
        return False
     if number <= 3:
        return True
     if number % 2 == 0 or number % 3 == 0:
        return False
     i = 5
     while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
     return True

def multipl_table():
    start = 1
    end = 10
    for i in range(start, end + 1):
        for j in range(1, 11):
            product = i * j
            print(f"{i} x {j} = {product}")
def multipl_table_in_range(num_1, num_2):
    for i in range(num_1, num_2 + 1):
        for j in range(1, 11):
            product = i * j
            print(f"{i} x {j} = {product}")
if __name__ == "__main__":
    #calculate(2, 23)
    #multipl_table()
    print("Enter first range: ")
    num1 = int(input())
    print("Enter second range: ")
    num2 = int(input())
    multipl_table_in_range(num1, num2)
   