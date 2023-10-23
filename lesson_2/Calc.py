import math
print("Select an operation:")

#exit = input("Press q to exit")
action = input()
num_1 = int(input("Enter first num please:"))
num_2 = int(input("Enter second num please:"))
flag = True


def addition():
        print("Result:", num_1 + num_2)

def sub():
        print("Result", num_1 - num_2)

def div():
    try:
        print("Result", num_1 / num_2)
    except ZeroDivisionError:
        print("Zero division error")

# while action != " ":
#     if(action == " " and exit == "q"):
#          break
#     elif(action == '+'):
#         addition()
#     elif(action == "-"):
#         sub()
#     elif(action == "/"):
#         div()
  
while flag == True:
    
        if action == '+':
            addition()
            break
        
        elif action == "-":
            sub()
            
        elif action == "/":
            div()
            
        if action=='q':
            break
            
        
             
    

