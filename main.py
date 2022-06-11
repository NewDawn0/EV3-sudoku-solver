#!/usr/bin/env pybricks-micropython
# ===> Imports & Libraries
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import *
from pybricks.parameters import Port, Stop, Direction, Button
from pybricks.tools import wait, StopWatch
from pybricks.media.ev3dev import SoundFile, ImageFile
import os

# ===> Constants & Global Variables
board = [ #                     
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
ev3 = EV3Brick()
motorX = Motor(Port.A)
motorY = Motor(Port.B)

factorX = 1000/3
factorX2 = 1000/3
factorY = 900/9
factorY2 = 1800/9

xpos = 0
ypos = 0

Board = os.system('curl -s 172.19.35.174:3000/api/boardOut | grep -o "[0-9]*" > io.txt')

# ===> Functions & Classes
# assembleBoard
def assembleBoard(board):
    with open('io.txt', 'rb') as f:
        for i in range(9):
            for j in range(9):
                num = int(f.readline())
                board[i][j] = num
    return board

# goto function
def goto(x, y):
    global xpos, ypos
    relX = 1.5*x - xpos
    relY = 2*y - ypos
    if relX < 0:
        # back
        motorX.run_time(speed=1000, time=abs(relX*factorX))
    elif relX > 0:
        # forward
        motorX.run_time(speed=-1000, time=abs(relX*factorX2))
    if relY < 0:
        motorY.run_time(speed=500, time=abs(relY*factorY))
    elif relY > 0:
        motorY.run_time(speed=-500, time=abs(relY*factorY2))
    xpos = x
    ypos = y

# print Board
def printBoard(board):
    for line in range(len(board)):  #                         <--.
        if line % 3 == 0 and line != 0:  # check every 3rd line  |- print horizontal lines
            print("------------------------- ")  #            <--^

        for char in range(len(board[0])):  #                 <--.
            if char % 3 == 0 and char != 0:  #                  |- print vertical lines
                print(" | ", end="")# end="" -> no new lines <--^

            if char == 8:  # check if at the end of line     <--.
                print(board[line][char])  #                     |- print numbers
            else:  #                                            |
                print(board[line][char], end=" ")  #         <--^

# Check if number is valid
def checkValidBoard(board): #
    for num in range(1, 10): #                               <--.
        varList = [] #                                          |-loop over numbers
        # loop over lines                                   <--^
        for line in range(len(board)):  # loop over lines    <--.
            for char in range(len(board[0])): #                 |
                if board[line][char] == num: #                  |
                    varList.append(num) #                       |
            if varList.count(num) > 1:  #                       |- check numbers in lines for Validity
                varList.clear() #                               |
                return False #                                  |
            else: #                                             |    
                varList.clear() # clear list                 <--^
        # loop over collumns
        for col in range(len(board[0])):# loop over collumns <--.
            for line in range(len(board)): #                    |
                if board[line][col] == num: #                   |
                    varList.append(num)  #                      |
            if varList.count(num) > 1:  #                       |- check collumns for Validity
                varList.clear()  #                              |
                return False  #                                 |
            else:  #                                            |
                varList.clear() # clear list                 <--^
        # loop over boxes
        for x in range(len(board)): # loop over boxes        <--.
            for y in range(len(board[0])): #                    |
                boxX = x // 3 #                                 |
                boxY = y // 3 #                                 |
                for row in range(boxY*3, boxY*3+3): #           |
                    for col in range(boxX*3, boxX*3+3): #       |
                        if board[row][col] == num: #            |- check boxes
                            varList.append(num) #               |
                if varList.count(num) > 1: #                    |
                    varList.clear() #                           |
                    return False #                              |
                else: #                                         |
                    varList.clear() # clear list             <--^
    return True

def getValid(board, val, pos):
    for row in range(len(board[0])): #                       <--.
        # check if number already exists in row                 |
        #  ,-----------^------------,                           |
        if board[pos[0]][row] == val and pos[1] != row: #       |- check if number exists in row
            #                            `------v------`        |
            #       check if number wasn't inserted in field    |
            return False  #                                  <--^

    for col in range(len(board)):  #                         <--.
        # check if number already exists in row                 |
        #  ,------------^-------------,                         |
        if board[col][pos[1]] == val and pos[0] != col:  #      |- check if number exists in collumn
            #                                 `------v------`   |
            #      check if number wasn't inserted in field     |
            return False  #                                  <--^

    boxX = pos[1] // 3  # int division (auto round down)     <--.
    boxY = pos[0] // 3  # int divsion (auto round down)         |
    #                                                           |
    # loop over rounded row value                               |
    for row in range(boxY*3, boxY*3+3):  #                      |- check if number exists in box
        #                                                       |
        # loop over rounded collumn value                       |
        for col in range(boxX*3, boxX*3+3):  #                  |
            if board[row][col] == val and (row, col) != pos:  # |
                return False  #                              <--^
    return True  #                                           <-- else return True

# Check if field is free
def getFree(board):
    for line in range(len(board)):  # loop over lines        <--.
        # loop over rows                                        |
        for col in range(len(board[0])):  #                     |- check for free fields
            if board[line][col] == 0:  # check if field is free |
                return (line, col)  # return all free fields <--^

    return None

# ===> Main Function
# main -> Recursive function using backtracking to fill up board


def main(board):
    free = getFree(board)  # check if there are free fields
    if not free:  # checks if all fields are full            <--.-check if board is full
        return True  # solution found                        <--^

    else: #                                                  <--.-assign row and collumn to the output of getFree
        row, col = free  #                                   <--^    therefore storing the position of a free field

    for val in range(1, 10): #                               <--.
        if getValid(board, val, (row, col)): #                  |
            board[row][col] = val  # number in board            |
            #                    to possible value              |
            #                                                   |- loop over the board and fill it in
            if main(board):  # call this function again         |
                return True  #                                  |
            else:  # if the value is false                      |
                board[row][col] = 0  # reset last entered       |
                # value in board                             <--^

    return False  # <-- else return False

# ===> Running Functions
# start programm
if __name__ == '__main__': #                                 <-- run main function if programm is called directly
    ev3.speaker.beep() # play sound to indicate start        <--.
    ev3.speaker.say("Solving Board") # say "Solving Board"      |
    ev3.speaker.say("Please wait") # speak     |- Print to EV3 screen and speak
    ev3.screen.clear() # clear screen                           |
    ev3.screen.print("Solving Board...") # print to screen   <--^
    board = assembleBoard(board)  # assemble board
    print("Raw Input") # raw input                           <--.
    printBoard(board) # print the board given as input          |- print the board given as input
    print() # free empty                                     <--^
    if checkValidBoard(board):
        ev3.speaker.beep()  # play to indicate done.             |
        main(board)  # solve board
        print("Solution")  # |- print the solution
        printBoard(board)  # print solved board               <--^
        for a in range(len(board)):  # loop over lines        <--.
            for b in range(len(board[0])):  # loop over tiles    |
                goto(0, -3.8)  # go to next tile                |
                ev3.speaker.say(str(board[a][b]))  # speak number |
                # clear screen               |- speak and print the current number on the tile
                ev3.screen.clear()
                ev3.screen.print(str(board[a][b]))  # <--^
            for c in range(0, 9):  # <--.
                # loop over tiles to go back to beginning of line   |- return to beginning of line and go to next line
                goto(0, 1.27)  # move back one tile              |
            goto(2.2, 0)  # go to next line                   <--^
        for i in range(0, 9):  # loop over line to            <--.
            # go back to the beginning of the board (position 0 0)  |- return to beginning of board
            goto(-3.43, 0)  # move back one line              <--^

        ev3.speaker.beep()  # play sound to indicate end      <--.
        # say "Board solved"    |- play sound to indicate end
        ev3.speaker.say("Board solved")
        ev3.screen.print("Board solved")  # print to screen      |
        wait(1000)  # wait 1 second                              |
        ev3.screen.clear()  # |
        printBoardScreen(board)  # print to screen            <--^
        wait(5000)  # wait 5 seconds
    else: #                                                  <--.
        ev3.speaker.beep()  # play to indicate done.             |- print the board given as input
        # say no solution  |  check if a solution was found
        ev3.speaker.say("Invalid Board")
        ev3.screen.clear()  # clear screen                       |
        ev3.screen.print("Invalid Board")  # <--^
        wait(5000)  # wait 5 seconds
        exit(1)
