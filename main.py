
def main():
    print("Welcome to 4 in a row.")
    turn = "X"
    table = [[0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0] ]
    winner = 0
    while winner == 0:
        if turn == "X":
            print("Player 1, choose a column (1-7) to place token.")
            token = int(input("Column: "))
            success = canPlace(token, table)

            while not success:
                print("Player 1, choose a column (1-7) to place token. Again")
                token = int(input("Column: "))
                success = canPlace(token, table)

            table = place(token, table, turn)
            printTable(table)

            win = checkForWin(table,turn)

            if win:
                print("Player 1, you have won!")
                break
            turn = "O"

        if turn == "O":
            print("Player 2, choose a column (1-7) to place token.")
            token = int(input("Column: "))
            success = canPlace(token, table)

            while not success:
                print("Player 2, choose a column (1-7) to place token. Again")
                token = int(input("Column: "))
                success = canPlace(token, table)

            table = place(token, table, turn)
            printTable(table)

            win = checkForWin(table,turn)

            if win:
                print("Player 2, you have won!")
                break
            turn = "X"


def canPlace(token, table):
    if token < 1 or token > 7:
        return False
    if table[0][token-1] == 0 or table[1][token-1] == 0 or table[2][token-1] == 0 or table[3][token-1] == 0 or table[4][token-1] == 0 or table[5][token-1] == 0:
        return True
    else:
        return False

def place(token, table, turn):
    for i in range(5,-1,-1):
        if table[i][token-1] == 0:
            if turn == "X":
                table[i][token-1] = "X"
                return table
            else:
                table[i][token - 1] = "O"
                return table


def printTable(table):
    for i in range(6):
        print(table[i])


def checkForWin(table, turn):
    if turn == "X":
        for i in range(6):
            for j in range(7):
                if table[i][j] == "X":
                    if singleCheck(i, j, turn, table):
                        return True
        return False
    else:
        for i in range(6):
            for j in range(7):
                if table[i][j] == "O":
                    if singleCheck(i, j, turn, table):
                        return True
        return False

def singleCheck(i, j, turn, table):
    if i+3 <= 5 and table[i][j] == turn and table[i+1][j] == turn and table[i+2][j] == turn and table[i+3][j] == turn:
        return True
    elif i-3 >= 0 and table[i][j] == turn and table[i-1][j] == turn and table[i-2][j] == turn and table[i-3][j] == turn:
        return True
    elif j+3 <= 6 and table[i][j] == turn and table[i][j+1] == turn and table[i][j+2] == turn and table[i][j+3] == turn:
        return True
    elif j-3 >= 0 and table[i][j] == turn and table[i][j-1] == turn and table[i][j-2] == turn and table[i][j-3] == turn:
        return True
    elif i+3 <= 5 and j+3 <= 6 and table[i][j] == turn and table[i+1][j+1] == turn and table[i+2][j+2] == turn and table[i+3][j+3] == turn:
        return True
    elif i-3 >= 0 and j+3 <= 6 and table[i][j] == turn and table[i-1][j+1] == turn and table[i-2][j+2] == turn and table[i-3][j+3] == turn:
        return True
    elif i+3 <= 5 and j-3 >= 0 and table[i][j] == turn and table[i+1][j-1] == turn and table[i+2][j-2] == turn and table[i+3][j-3] == turn:
        return True
    elif i-3 >= 0 and j-3 >= 0 and table[i][j] == turn and table[i-1][j-1] == turn and table[i-2][j-2] == turn and table[i-3][j-3] == turn:
        return True

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
