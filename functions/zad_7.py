# # def is_happy_number(n):
# #     seen_numbers = set()
# #     while n != 1 and n not in seen_numbers:
# #         seen_numbers.add(n)
# #         n = sum(int(digit)**2 for digit in str(n))
# #     return n == 1

# # number = int(input("Введите число: "))
# # if is_happy_number(number):
# #     print(f"{number} - счастливое число!")
# # else:
# #     print(f"{number} - не счастливое число.")

# def happyNumber(num:int):
#     strnum = str(num)
#     if len(strnum) != 6:
#         print("err")
#     else:
#         if(int(strnum[0] + int(strnum[1] + strnum[2])) == int((strnum[3] + strnum[4] + strnum[5])):
#               print("happyNumber")
#               else:
#               print("net") 