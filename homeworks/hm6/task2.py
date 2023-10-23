def main():
    str = input("Enter text please: ")
    text = str.split()
    rezerved_words = input("Enter reserving words: ")
    for i in range(len(text)):
        if text[i] in rezerved_words:
            text[i] = text[i].upper()
    rezult_text = "".join(text)
    print(rezult_text)
           
                


if __name__ == "__main__":
    main()
