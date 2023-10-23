def func(num_1, num_2):
    sum = 0
    for i in range(num_1, num_2 + 1):
        sum += i
    print(sum)

if "__main__" == __name__:
    func(4, 6)