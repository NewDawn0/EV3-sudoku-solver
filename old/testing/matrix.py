# ===> Constants & Global Variables
# <Variable description>
position = (0, 0)


# ===> Functions & Classes
# <Function description>
def goto(x, y, position):
    globals()['position'] = (x, y)
    relX = x - position[0]
    relY = y - position[1]
    position = (x, y)
    move(relX, relY)

def move(x, y):
    print(f"moving {x}, {y}")
    #print(f"moving {x}")
    #print(f"moving {y}")

# ===> Main Function
def main():
    scanField()
    goto(0, 0, (position)) # reset position

def scanField():
    for y in range(0, 9):
        for x in range(0, 9):
            goto(x, y, (position))

def drawPosition(board):
    for line in range(len(board)):
        for char in range(len(board[line])):
            num = (board[line][char])
            goto(char, line, (position))
            if num == 1:
                num1.draw()
            elif num == 2:
                num2.draw()
            elif num == 3:
                num3.draw()
            elif num == 4:
                num4.draw()
            elif num == 5:
                num5.draw()
            elif num == 6:
                num6.draw()
            elif num == 7:
                num7.draw()
            elif num == 8:
                num8.draw()
            elif num == 9:
                num9.draw()
            else:
                print("ERROR: Invalid number")
                exit(-1)


# ===> Execute Main Function
if __name__ == '__main__':
    main()
