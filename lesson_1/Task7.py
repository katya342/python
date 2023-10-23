if __name__ == "main": 
 
    def display_board(board, start_position=None, end_position=None): 
        print("  a b c d e f g h") 
        print(" -----------------") 
 
        for i in range(8): 
            print(i + 1, end="|") 
            for j in range(8): 
                if (j + i) % 2 == 0: 
                    print("$" + board[i][j], end="") 
                else: 
                    print(board[i][j], end=" ") 
 
                print("|" + str(i + 1)) 
        print(" --------------") 
        print("  a b c d e f g h")