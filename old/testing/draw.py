# ===> Imports & Libraries
from modules.movement import *
# ===> Constants & Global Variables
# config variables
scale = 2
midOffset = 10

# number constructor class
class Number: #
    # Class variables

    # self
    def __init__(self, X, Y): #                                                 |- A Number object constructor
        self.X = X #                                                                  | requiring that every "Number" has an X and Y Value
        self.Y = Y #
        self.skip = [0, (len(self.X))-1]

    # class functions
    def draw(self):
        index = 0
        for x, y in zip(self.X, self.Y):
            if index in self.skip:
                penup()
            else:
                pendown()
            goto(x*scale, y*scale)
            index += 1

    def extendSkip(self, extend):
        for value in extend:
            value = int(value)
            self.skip.append(value)

def movR():
    penup()
    goto(midOffset*scale, 0)
    pendown()

def movL():
    penup()
    goto(-midOffset*scale, 0)
    pendown()

def movU():
    penup()
    goto(0, midOffset*scale)
    pendown()

def movD():
    penup()
    goto(0, -midOffset*scale)
    pendown()

def nl():
    movD()
    for i in range(1, 11):
        movL()

def nbl(): # new block line
    movD()


# number objects
num1 = Number([-2, 4, 0, -2], [2, 2, -8, 4])  # <--.
num2 = Number([-3, 2, 2, 2, -6, 6, -3], [2, 2, 0, -2, -6, 0, 4])  # |
num3 = Number([-3, 2, 2, 2, -2, 2, -2, -2, -2, 3], [2, 2, 0, -2, -2, -2, -2, 0, 2, 2])
num4 = Number([-3, 0, 6, -2, 0, -1], [4, -4, 0, 4, -8, 4])
num4.extendSkip([3, 5])
num5 = Number([3, -6, 0, 4, 2, 0, -2, -2, -2, 3], [4, 0, -2, 0, -2, -2, -2, 0, 2, 2])# |- Number objects containing all points
num7 = Number([-2, 4, -1, -2, -1, 2], [4, 0, -3, -2, -3, 4]) #                         |    relative to the previous point
num9 = Number([-3, 2, 2, 2, 0, -2, -2, -2, 0, 2, 2, 2, -3], #                          |
              [-2, -2, 0, 2, 4, 2, 0, -2, -2, -2, 0, 2, 0]) #                          |
num8 = Number([-1, -2, 2, 2, 2, -2, -2, -2, 2, 2, 2, -2, -1], #                        |
              [0, 2, 2, 0, -2, -2, 0, -2, -2, 0, 2, 2, 0]) #                           |
num6 = Number([3, -2, -2, -2, 0, 2, 2, 2, 0, -2, -2, -2, 3], #                         |
              [2, 2, 0, -2, -4, -2, 0, 2, 2, 2, 0, -2 , 0]) #                       <--^