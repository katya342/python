def main(action):
    if(action == "1"):
        book_names.sort()
        print(book_names)
    if(action == "2"):
        book_dates.sort()
        print(book_dates)
    if(action == "3"):
        for name, year in zip(book_names, book_dates):
             print(f"{name} ({year})")
    
def menu():
    print("1/ Sorting by book name")
    print("2/ Sorting by dates")
    print("3/ Printing book info")
    print("q/ Exit")
    action = input()
    return action

if __name__ == "__main__":
    book_names = ["Martin Eden", "Portrait of Dorian Gray", "Shantaram", "Letter of unknown"]
    book_dates = [2002, 2001, 1999, 2012]
    while True:
        temp = menu()
        if temp == "q":
            break
        main(temp)
    