
def function(dlina, direction, symbol):

    if(direction == 1):
        for i in range(dlina):
            print(symbol, end=" ")
    else:
        for i in range(dlina):
            print(symbol)
   

if "__main__" == __name__:
    function(10, 2, "-")