def main():
    a = int(input("Enter num_1: "))
    b = int(input("Enter num_2: "))
    c = int(input("Enter num_3: "))
    action = input("Enter action.. (1) - sum, (2) - multiply")
    if(action == "1"):
        print(f"Rezult: {a + b + c}")
    else:
        print(f"Rezult: {a * b * c}")


if __name__ == "__main__":
    main()




