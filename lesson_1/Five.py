number1 = int(input("Enter the number1")) 
number2 = int(input("Enter the number2")) 
print("What do you want?") 
print("1. Sum of the numbers") 
print("2. Razniza") 
print("3. SredneArifmeticheskoe") 
print("4. Proizvedenie") 
 
enter = int(input("Enter what do you want")) 
if enter == 1: 
    result = number1 + number2 
    print("Result", result) 
elif enter == 2: 
    if number1 > number2: 
        print("Number1 is even", number1) 
    else: 
        print("Number2 is even", number2) 
elif enter == 3: 
    result = (number1 + number2) / 2 
    print("Result", result) 
elif enter == 4: 
    result = number1 * number2 
    print("Result", result)