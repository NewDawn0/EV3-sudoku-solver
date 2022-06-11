#!/usr/bin/env pybricks-micropython
# ===> Imports & Libraries
import subprocess

# ===> Constants & Global Variables
board = [
    [0, 0, 5, 0, 0, 0, 4, 0, 0],
    [0, 7, 0, 5, 0, 8, 0, 9, 0],
    [2, 0, 0, 0, 7, 0, 0, 0, 8],
    [4, 0, 9, 0, 0, 0, 1, 0, 3],
    [0, 0, 0, 0, 2, 0, 0, 0, 0],
    [5, 0, 6, 0, 0, 0, 9, 0, 4],
    [9, 0, 0, 0, 3, 0, 0, 0, 5],
    [0, 4, 0, 2, 0, 7, 0, 1, 0],
    [0, 0, 3, 0, 0, 0, 6, 0, 0]
]
solvedBoard = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# ===> Functions & Classes
def printBoard(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("------┼-------┼------")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def writeBoard():
    f = open("io.txt", "a")
    for line in range(len(board)):
        for char in range(len(board[line])):
            num = (board[line][char])
            f.write(str(num) + "\n")
    f.close()

def clearFile():
    with open("io.txt", "r+") as f:
        f.truncate(0)


def calculate():
    # calculate the solution
    process = subprocess.Popen('./main', stdout=subprocess.PIPE)
    out, err = process.communicate()
    out = out.decode('utf-8')
    # get output
    for i, char in enumerate(out):
        if 0 <= i <= 8:
            solvedBoard[0][i] = int(char)
        elif 9 <= i <= 17:
            solvedBoard[1][i - 9] = int(char)
        elif 18 <= i <= 26:
            solvedBoard[2][i - 18] = int(char)
        elif 27 <= i <= 35:
            solvedBoard[3][i - 27] = int(char)
        elif 36 <= i <= 44:
            solvedBoard[4][i - 36] = int(char)
        elif 45 <= i <= 53:
            solvedBoard[5][i - 45] = int(char)
        elif 54 <= i <= 62:
            solvedBoard[6][i - 54] = int(char)
        elif 63 <= i <= 71:
            solvedBoard[7][i - 63] = int(char)
        elif 72 <= i <= 80:
            solvedBoard[8][i - 72] = int(char)
        else:
            pass    



# ===> Running Functions
if __name__ == '__main__':
    printBoard(board)
    print()
    clearFile()
    writeBoard()
    calculate()
    printBoard(solvedBoard)
    #drawPosition(solvedBoard)
