

def count_apples(days: int, apples_in_basket: int) -> int:
    # for i in range(days):
    #     apples_in_basket += 1
    # print(apples_in_basket)
    if days == 0:
        return apples_in_basket
    return(count_apples(days - 1, apples_in_basket + 1))


if __name__ == "__main__":
   print(count_apples(5, 0))