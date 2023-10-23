def calculate(str : str):
    sign = ["+", "-", "*", "/"] 
    for item in str:
        if item in sign:
            symbol = item
            if(symbol == "+"):
                splited_string = str.split("+")
                return int(splited_string[0]) + int(splited_string[1])
            elif(symbol=="-"):
                splited_string = str.split("-")
                return int(splited_string[0]) - int(splited_string[1])
            elif(symbol == "*"):
                splited_string = str.split("*")
                return int(splited_string[0]) * int(splited_string[1])
            elif(symbol == "/"):
                splited_string = str.split("/")
                return int(splited_string[0]) / int(splited_string[1])



if __name__ == "__main__":
   print("Enter arithmetical expression: ")
   temp = input()
   print(calculate(temp))
