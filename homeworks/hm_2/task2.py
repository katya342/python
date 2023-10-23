def main():
    a = int(input("Enter num_1: "))
    b = int(input("Enter num_2: "))
    c = int(input("Enter num_3: "))
    action = input("Enter action.. (1) - minimum, (2) - maximum, (3) - average")
    if(action == "1"):
            maximum = max(a, b, c)
            print(f"Minimum is: {maximum}")
    if(action == "2"):
            minimum = min(a, b, c)
            print(f"Maximum is {minimum}")
    if(action == "3"):
        average = (a + b + c) / 3
        print(f"Average is: {average}")

if __name__ == "__main__":
    main()
