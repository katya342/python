def is_vowel(letter):
    vowels = ['y', 'e', 'ы', 'ё', 'я', 'о', 'и']

    if letter in vowels:
        return True
    else:
        return False
def salt_language(lines) -> str:
    new_line = ""
    lines = lines.lower()
    list_lines = list(lines.split(" "))

    for word in list_lines:
        for value in word:
            if(is_vowel(value)):
                new_line += value + "c" + value
            else:
                new_line += value
        new_line += " "
    return new_line.capitalize()

def main():
    print(salt_language("Папе не ты"))

if __name__ == "__main__":
    main()