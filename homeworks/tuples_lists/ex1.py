def tuples():
    tuple_1 = (1, 2 , 3, 5, 6)
    tuple_2 = (2, 1, 5, 6)
    tuple_3 = (4, 2, 9, 23, 5, 1, 3, 6)
    temp = set(tuple_1)
    set(tuple_2)
    set(tuple_3)
    value = temp.intersection(tuple_2, tuple_3, tuple_1)
    print(value)
def tuples_2():
    tuple_1 = (1, 2 , 3, 5)
    tuple_2 = (2, 1, 5, 6)
    tuple_3 = (4, 2, 9, 23)
    temp = set(tuple_1)
    temp_2 = set(tuple_2)
    temp_3 = set(tuple_3)
    value = temp.difference(tuple_2, tuple_3)
    print(f"Unique elements in tuple 1: {value}")
    value_2 = temp_2.difference(tuple_1, tuple_3)
    print(f"Unique elements in tuple 2: {value_2}")
    value_3 = temp_3.difference(tuple_1, tuple_2)
    print(f"Unique elements in tuple 3: {value_3}")

def tuples_3():
    tuple_1 = (1, 2 , 3, 5, 6, 6, 7, 7, 22, 223, 22)
    tuple_2 = (1, 1, 5, 6, 6, 6, 7, 7, 22)
    tuple_3 = (1, 2, 9, 23, 6, 6, 7, 7, 7, 19, 22)
    val_1 = list(tuple_1)
    val_2 = list(tuple_2)
    val_3 = list(tuple_3)
    for i in range(len(val_1)):
        for j in range(len(val_2)):
            for k in range(len(val_3)):
                if(val_1[i] == val_2[j] == val_3[k] and i == j == k):
                    print(f"Elem value: {val_1[i]} in the same position: {i}")
        

if __name__ == "__main__":
    #tuples_2()
    tuples_3()
