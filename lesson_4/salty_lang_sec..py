LOWER = ["а", "я", "у", "ю", "о", "е", "ё", "э", "и", "ы"] 
UPPER = ["А", "Я", "У", "Ю", "О", "Е", "Ё", "Э", "И", "Ы"] 
CHAR = "с"
 
def IsNullWord(wordd) -> bool: 
    if wordd != "": 
        return True 
    else: 
        return False 

def salt(sentence: str) -> str:

    for vowel in LOWER + UPPER:
        sentence = sentence.replace(vowel, vowel + CHAR +  vowel.lower())

    return sentence
  
def main():
    print("Соленный язык")
    print(salt(input("Введите русское слово: ")))

if __name__ == "main":
    main()