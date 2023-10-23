def count_fruits(fruits, fruit):
    return fruits.count(fruit)

def replace_manufacturer(tup: tuple, manufacturer: str, replacement:str) -> tuple:
    return tuple(replacement if item == manufacturer else item for item in tup)

def counting_tuple(nums):
    one,two,three = 0,0,0
    for num in nums:
        if len(str(num)) == 1: one+=1
        elif len(str(num)) == 2: two+=1
        elif len(str(num)) == 3: three+=1
    print(f"Одна цифра - {one} элементов, \n две цифры - {two}, \n три цифры - {three}")

if "__main__" == __name__:
    numbers = (1, 5, 553, 29, 110, 1, 453, 22, 345, 1, 1234)
    counting_tuple(numbers)
    # fruits = ('banana', 'mango', 'apple', 'bananaapple', 'bananamango', 'mangobanana')
    # fruit = input()
    # count = 0
    # for val in fruits:
    #     if(count_fruits(val, fruit)):
    #         count +=1
    # print(f"Фрукт {fruit} встречается {count} раз")
    # brand = input()
    # replacement = input()
    # cars = ('BMW', 'Toyota', 'BMW')
   
    # print(replace_manufacturer(cars, brand, replacement))
   # print(f"Фрукт {fruit} встречается {count_fruits(fruits, fruit)} раз в кортеже")
    