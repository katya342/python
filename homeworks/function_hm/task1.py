
def info():
    print("Don't let the noise of others' opinions \ndrown out your own inner voice.\n                           Steve Jobs")

def odd_nums(num_1, num_2):
    for i in range(num_1, num_2):
        if(i % 3 == 0):
            print(f"Odd num: {i}")


def linia(dlina, direction, symbol):
    if(direction == "vertically"):
        for i in range(dlina):
            print(symbol)
    else:
        print(symbol * dlina)

def maximum(num_1, num_2, num_3, num_4):
    print(max(num_1, num_2, num_3, num_4))
def is_prime(number):
    if number <= 1:
        return False 
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False 

    return True  
   

def summ_in_range(num_1, num_2):
    sum = 0
    for i in range(num_1, num_2 + 1):
        sum += i
    print(sum)

def lucky_num(number):
    temp = str(number)
    substring_1 = temp[0: 3]
    substring_2 = temp[3: 7]
    sum = 0
    sum_2 = 0
    for i in substring_1:
        sum += int(i)
    for j in substring_2:
        sum_2 += int(j)

    if(sum == sum_2):
        print("LUCKY NUMBER")
    else:
        print("UNLUCKY")
        

if __name__ == "__main__":
    # info()
    # odd_nums(2, 10)
    # linia(10, "horizontally", "@")
    # maximum(3, 4, 5, 6)
    #summ_in_range(3, 7)
    # is_prime(4)
    lucky_num(123420)

