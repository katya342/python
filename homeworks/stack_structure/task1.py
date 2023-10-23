def main():
    numbers = []
    
    while True:
        print("Menu:")
        print("1. Add a new number to the list")
        print("2. Remove all occurrences of a number from the list")
        print("3. Show the contents of the list (forward or reverse)")
        print("4. Check if a value is in the list")
        print("5. Replace a value in the list")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            number = int(input("Enter a number to add: "))
            if number not in numbers:
                numbers.append(number)
            else:
                print("Number already exists in the list.")

        elif choice == '2':
            number = int(input("Enter a number to remove: "))
            while number in numbers:
                numbers.remove(number)

        elif choice == '3':
            if not numbers:
                print("The list is empty.")
            else:
                direction = input("Show list forward (F) or reverse (R)? ").upper()
                if direction == 'F':
                    print("List:", numbers)
                elif direction == 'R':
                    print("Reversed List:", numbers[::-1])

        elif choice == '4':
            number = int(input("Enter a number to check: "))
            if number in numbers:
                print(f"{number} is in the list.")
            else:
                print(f"{number} is not in the list.")

        elif choice == '5':
            number = int(input("Enter a number to replace: "))
            new_number = int(input("Enter the new number: "))
            replace_all = input("Replace all occurrences? (Y/N): ").upper()
            if replace_all == 'Y':
                for i in range(len(numbers)):
                    if numbers[i] == number:
                        numbers[i] = new_number
            else:
                if number in numbers:
                    index = numbers.index(number)
                    numbers[index] = new_number
                else:
                    print(f"{number} is not in the list.")
        
        elif choice == '6':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
