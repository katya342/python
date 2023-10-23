
def sort_list(list: list):
    sum = 0
    size = int(len(list) * 2 / 3)
    size_2 = int(len(list) - (len(list) * 2 / 3))
    for item in list:
        sum += item
    arythmetic_average = sum / len(list)
    i = 0
    while i < size:
        temp = 0
        if arythmetic_average > 0 and list[i] > list[i + 1]:
            temp = list[i + 1]
            list[i+1] = list[i]
            list[i] = temp
            i = 0
        else:
            i += 1
            continue
    reversed_list = list[size:]
    reversed_list.reverse()
    print(reversed_list) 
    print(list)
    
def student_progress(action):
    if action == "1":
        print(list)
    if action == "2":
        #print("Enter index of elem in list: ")
        index = input("Enter index of elem in list: ")
        #print("Enter new mark: ")
        mark = input("Enter new mark: ")
        for i in range(int(len(list))):
            if i == int(index):
                list[i] = mark
    print(f"Rezulting marks: {list}")
    if action == "3":
        sum = 0
        average = 0
        for item in list:
            sum += int(item)
        average = sum / int(len(list))
        if average >= 10.7:
            print("Grand saved!")
        else:
            print("No grand")
    if action == "4":
        print(f"Sorted list: {list.sort(reverse=True)}")
def menu() -> str:
    print("1/ Printing marks")
    print("2/ Retake exams")
    print("3/ Grant check")
    print("4/ Printing sorted marks")
    action = input()
    return action


if __name__ == "__main__":
    #sort_list([4, 5, 6, 1, 2, 3, 10, 13, 2, 3, 0, 6, 9, 26])
    list=[]
    end = 12
    i = 0
    while i != 12:
        
        #print(f"Enter {i + 1} mark please: ")
        item = input(f"Enter {i + 1} mark please: ")
        list.append(item)
        i += 1
        
    temp = menu()
    student_progress(temp)