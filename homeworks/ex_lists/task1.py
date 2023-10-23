def main(action):
    if action == "1":
        ids.sort()
        print(ids)
    if action == "2":
        numbers.sort()
        print(numbers)
    if action == "3":
        for nums, id in zip(numbers, ids):
            print(f"Numbers: {nums} ids: {id}")
def menu():
    print("1/ Sorting by id code")
    print("2/ Sorting by mob number")
    print("3/ Printing users list")
    print("4/ Exit")
    action = input()
    return action

if __name__ == "__main__":
    ids = ["234542", "24325", "234255254352"]
    numbers = ["+774747", "+3253523", "823828382", "12323"]
    while True:
        temp = menu()
        if temp == "q":
            break
        main(temp)
    