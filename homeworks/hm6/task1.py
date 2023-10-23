def main():
    str = input("Enter string please: ")
    temp = str[::-1]
    if(str == str[::-1]):
        print("Palindrome")
    else:
        print("Ne palindrome")
  

if __name__ == "__main__":
    main()
