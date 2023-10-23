countr = {'usa', 'kazakhstan'}

def adding_countries(value):
    countr.add(value)
    print(countr)


def deleting_countries(value):
    countr.remove(value)
    print(countr)

def search_country(value):
    matching_countires = [item for item in countr if value in countr]
    return matching_countires and print('success')

def check_country_exists(value):
    return value in countr and print('country exists')

def sets_union(set_1, set_2):
    a.add("almatfzdy")
    b.add("parfis")
    temp = a.union(b)
    print(temp)



# def task_4(set_1, set_2):
#     a.add("almaty")
#     a.add("paris")
#     a.add("nyc")


#     b.add("paris")
#     b.add("kostanai")

#     rezult = a - b
#     return rezult and print(rezult)


def task_6(countr):
    countries_capitals.add("")


if "__main__" in __name__:

    countries_capitals = {
    "Россия": "Москва",
    "США": "Вашингтон, D.C.",
    "Китай": "Пекин",
    "Германия": "Берлин",
    "Франция": "Париж"
}
    task_6(countries_capitals)

     
   