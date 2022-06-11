#!/usr/bin/env pybricks-micropython
# ===> Imports & Libraries
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import *
from pybricks.parameters import Port, Stop, Direction, Button
from pybricks.tools import wait, StopWatch
from pybricks.media.ev3dev import SoundFile, ImageFile


# ===> Constants & Global Variables
board = [
    [0, 6, 0, 0, 7, 8, 0, 2, 0],
    [0, 0, 0, 9, 2, 0, 0, 7, 4],
    [0, 4, 0, 0, 5, 1, 6, 8, 0],
    [6, 2, 1, 0, 0, 3, 0, 0, 0],
    [3, 8, 0, 2, 6, 7, 0, 0, 0],
    [5, 0, 7, 0, 0, 0, 0, 3, 6],
    [4, 7, 0, 0, 3, 5, 9, 0, 2],
    [0, 1, 5, 7, 4, 9, 0, 0, 3],
    [0, 0, 0, 6, 0, 0, 0, 5, 7]
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

# ===> Functions & Classes
# printBoard to ev3 screen

def printBoardScreen(board):
    for line in range(len(board)):
        ev3.screen.print(str(board[line][0]) + " " + str(board[line][1]) + " " + str(board[line][2]) + " " + str(board[line][3]) + " | " + str(board[line][4]) + " " + str(board[line][5]) + " " + str(board[line][6]) + " | " + str(board[line][7]) + " " + str(board[line][8]))

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
    for line in range(len(board)): #                         <--.
        if line % 3 == 0 and line != 0: # check every 3rd line  |- print horizontal lines
            print("------------------------- ") #            <--^

        for char in range(len(board[0])): #                  <--.
            if char % 3 == 0 and char != 0: #1                   |- print vertical lines
                print(" | ", end="")# end="" -> no new lines <--^

            if char == 8: # check if at the end of line      <--.
                print(board[line][char]) #                      |- print numbers
            else: #                                             |
                print(board[line][char], end=" ") #          <--^

# Check if number is valid
def getValid(board, val, pos):
    for row in range(len(board[0])):  #                      <--.
        # check if number already exists in row                 |
        #  ,-----------^------------,                           |
        if board[pos[0]][row] == val and pos[1] != row: #       |- check if number exists in row
            #                            `------v------`        |
            #       check if number wasn't inserted in field    |
            return False #                                   <--^


    for col in range(len(board)): #                          <--.
        # check if number already exists in row                 |
        #  ,------------^-------------,                         |
        if board[col][pos[1]] == val and pos[0] != col: #       |- check if number exists in collumn
        #                                 `------v------`       |
        #           check if number wasn't inserted in field    |
            return False #                                   <--^

    boxX = pos[1] // 3 # int division (auto round down)      <--.
    boxY = pos[0] // 3 # int divsion (auto round down)          |
    #                                                           |
    # loop over rounded row value                               |
    for row in range(boxY*3, boxY*3+3): #                       |- check if number exists in box
        #                                                       |
        # loop over rounded collumn value                       |
        for col in range(boxX*3, boxX*3+3): #                   |
            if board[row][col] == val and (row, col) != pos: #  |
                return False #                               <--^

    return True #                                            <-- else return True

# Check if field is free
def getFree(board):
    for line in range(len(board)):  # loop over lines        <--.
        for col in range(len(board[0])): # loop over rows       |- check for free fields
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
        row, col = free #                                    <--^    therefore storing the position of a free field

    for val in range(1, 10): #                               <--.
        if getValid(board, val, (row, col)): #                  |
            board[row][col] = val # number in board             |
            #                    to possible value              |
            #                                                   |- loop over the board and fill it in
            if main(board): # call this function again          |
                return True #                                   |
            else: # if the value is false                       |
                board[row][col] = 0 # reset last entered        |
                # value in board                             <--^

    return False #                                           <-- else return False


# ===> Running Functions
# start programm
if __name__ == '__main__': #                                 <-- run main function if programm is called directly
    ev3.speaker.beep() # play sound to indicate start        <--.
    ev3.speaker.say("Solving Board") # say "Solving Board"      |
    ev3.speaker.say("Please wait about 40 seconds") # speak     |- Print to EV3 screen and speak
    ev3.screen.clear() # clear screen                           |
    ev3.screen.print("Solving Board...") # print to screen   <--^
    print("Raw Input") # raw input                           <--.
    printBoard(board) # print the board given as input          |- print the board given as input
    print() # free empty                                     <--^

    main(board) # solve board
    if board[8][8] == 0: # check if the last field is empty   <--.
        ev3.speaker.beep() # play to indicate done.              |- print the board given as input
        ev3.speaker.say("No solution found") # say no solution   |- check if a solution was found
        ev3.screen.clear() # clear screen                        |
        ev3.screen.print("No solution found") #               <--^
        wait(5000)  # wait 5 seconds
        #   print("No solution found") # print no solution to screen
    else: #                                                   <--.
        ev3.speaker.beep() # play to indicate done.              |
        print("Solution") #                                      |- print the solution
        printBoard(board) # print solved board                <--^
        for a in range(len(board)): # loop over lines         <--.
            for b in range(len(board[0])): # loop over tiles     |
                goto(0, -3.8)  # go to next tile                 |
                ev3.speaker.say(str(board[a][b])) # speak number |
                ev3.screen.clear() # clear screen                |- speak and print the current number on the tile
                ev3.screen.print(str(board[a][b])) #          <--^
            for c in range(0, 9): #                           <--.
            # loop over tiles to go back to beginning of line    |- return to beginning of line and go to next line
                goto(0, 1.27) # move back one tile               |
            goto(2.2, 0) # go to next line                    <--^
        for i in range(0, 9): # loop over line to             <--.
        # go back to the beginning of the board (position 0 0)   |- return to beginning of board
            goto(-3.43, 0) # move back one line                <--^

        ev3.speaker.beep() # play sound to indicate end       <--.
        ev3.speaker.say("Board solved") # say "Board solved"     |- play sound to indicate end
        ev3.screen.print("Board solved") # print to screen       |
        wait(1000) # wait 1 second                               |
        ev3.screen.clear() #                                     |
        printBoardScreen(board) # print to screen             <--^
        wait(5000) # wait 5 seconds

