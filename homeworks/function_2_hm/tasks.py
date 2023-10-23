import math
def minimum_find(list):
    return min(list)
def double_list(list_1: list, list_2: list) -> list:
    return list_1 + list_2

def delete_value(list: list, num_1):
    temp = 0
    list_2 = []
    for item in list:
        if(item != num_1):
            list_2.append(item)
        else:
            temp += 1
    return temp

def function(num_1, list):
    newlist = []
    for i in list:
        i = math.pow(i, num_1)
        newlist.append(i)
        
    return newlist

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_prime_numbers(lst):
    prime_list = []
    for item in lst:
        if is_prime(item):
            prime_list.append(item)
    return prime_list
def multiply_nums(list: list):
    p = 1
    for item in list:
        p *= item
    return p
   
if __name__ == "__main__":
    # print(function(2, [2, 3, 4, 5]))
    # print(double_list([1, 2, 3 , 4], [5, 6, 7, 8]))
    # print(delete_value([1, 2, 2, 3, 4], 2))
    #print(find_prime_numbers([1, 2, 3, 4, 5, 6, 7, 10]))
    #print(minimum_find([1, 2, 3, 4]))
    print(multiply_nums([3, 2, 4]))