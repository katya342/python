def string_max_size() -> int:
    import sys
    return sys.maxsize

def line_breaks() -> None:
    text = "one\ntwo\nthree"
    print(text)
    return None

def concatenation() -> None:
    s1 = "Hello" + " world"
    s2 = " world"
    print(s1 + s2)

    name = "John"
    age = 30

    print("Name: " + name + ", age: " + str(age))

def index_string() -> None:
    s = "abcdef"
    print(s[0])
    print(s[1])
    print(s[2])

    print(s[-1])
    return None

def string_compare() -> None:
    s1 = "1a"
    s2 = "aa"
    s3 = "Aa"
    s4 = "ba"

    print("aa" < "Aa")
    print("aa" > "ba")
    print("aa" < "az")
    print(s1 > s2)
    print(s3 == s4)

    s1 = "Intel"
    s2 = "intel"
    print(s1 == s2)  #Регистр имеет значение
    print(s1.lower() == s2.lower()) #Приведение к нижнему регистру

    return None

def remove_string() -> None:
    s = "test"
    print(s, s.replace("test", ""))
    s = "test"
    s = ""
    print(s)
    return None

def custon_format_string() -> None:
    name = "Alex"
    print("Hello, %s" %name)

    print("%d %s, %d %s" % (6, "bananas", 10, "lemons"))

    print("{}".format(100))
    print("{0}, {1}, {2}".format("one", "two", "three"))

    print(f"Hello, {name}!")

    a = 5
    b = 10

    print(f"Five plus ten is {a + b} and not {2 * (a + b)}")
    return None

def quotation_marks() -> None: 
    print('string')
    print("string")
    print("""string""") #тройные кавычки 
    print('''string''') #тройные кавычки 

    print('book "war and peace"')   #разный тип кавычек
    print("book 'war and peace'")   #разный тип кавычек 
    print('book "war and peace"')   #экранирование кавычек  одного типа
    print("book 'war and peace'")   #экранирование кавычек  одного типа

    return None  

def string_methods() -> None:
    text = ("Wikipedia is a Python library that makes "
            "it easy to access and parse data from Wikipedia")
    print(text.find("Wikipedia"))
    print(text.rfind("Wikipedia"))
    print(text.count("Wikipedia"))

    print(
        text.replace("from Wikipedia", "from htttttt.org/")
    )
    print(text.split(" "))

    split_text = text.split(" ")
    print(split_text)
    print("_".join(split_text))

    text = "  test "
    print(text.strip()) #удаляет пробелы
    print(text.lstrip()) # удаляет пробелы в начале
    print(text.rstrip()) #удаляет пробелы в конце

    text = "Python is a product of the Python software foundation"
    print(text.lower())
    print(text.upper())
    text = "Python is a product of the oython soft found"

    print(text.capitalize())

    return None

def string_to_types() -> None:
    import json
    from datetime import datetime

    print(int("10"))
    print(int("0x12F", base=16))
    print("one two three four".split())

    print("one, two, three, four".split(","))
    print("Байты".encode("utf-8"))
    print(datetime.strptime("Jan 1 2020 1:33PM", "%b %d %Y %I:%M%p"))
    print(float("1.5"))
    print(
        json.loads('{"Russia": "Moscow", "France": "Paris"}')
    )
    print(json.dumps("hello"))
    return None

def best_practices() -> None:
    import re
    text = "django"
    print(list(text))
    print([c for c in "text"])

    for c in text:
        print(c)

    str = "h3110 23 cat 444.4 rabbit 11 2 dog"
    print([int(s) for s in str.split() if s.isdigit()])
    print(re.findall(r"\d+", str))
    print("test"[::-1])
    print("".join(reversed("test")))
    print("Some text1"[:-1])
    print(" Some text2 ".strip())
    print("So me t e x t ".replace(" ", " "))
    return None

def main() -> None:
    best_practices()
    

if __name__ == "__main__": 
    main()


