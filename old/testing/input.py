# ===> Imports & Libraries
#from modules.movement import *
#from modules.draw import *
from math import sqrt

# ===> Constants & Global Variables
# <Variable description>
val = 10.5
#turtle.color('black')
#turtle.hideturtle()
#turtle.pensize = 5
#turtle.speed(0)

# ===> Functions & Classes
# <Function description>
def movement():
    movR()
    done()


colors = [
    'white',
    'black',
    'red',
    'blue',
    'yellow',
    'green',
    'orange',
    'purple',
    'brown',
    'pink',
]
values = [
    759,
    6,
    257,
    257,
    508,
    257,
    422,
    462,
    247,
    294
]
edgeCases = [
    0,
    128,
    255,
]
def getEdgeCases(inputVal):
    for i in range(len(edgeCases)):
        minDiff = float('inf')  # define variabl
        closest = None
        for i in range(len(edgeCases)):
            diff = abs(edgeCases[i] - inputVal)
            if diff < minDiff:
                minDiff = diff
                closest = i 
        return edgeCases[closest]


def getColor(r, g, b, abience):
    r * abience
    g * abience
    b * abience
    distInput = (r^2)+ (g^2) + (b^2)
    minDiff = float('inf')  # define variabl
    closest = None
    for i in range(len(values)):
        diff = abs(values[i] - distInput)
        if diff < minDiff:
            minDiff = diff
            closest = i
            if closest == 2:
                rVal = getEdgeCases(r)
                gval = getEdgeCases(g)
                bval = getEdgeCases(b)
                if rVal == 255 and gval == 0 and bval == 0:
                    return 'red'
                elif rVal == 0 and gval == 255 and bval == 0:
                    return 'green'
                elif rVal == 0 and gval == 0 and bval == 255:
                    return 'blue'
                elif rVal == 128 and gval == 0 and bval == 128:
                    return 'purple'
                else:
                    pass
                    #print('color determination failed')
                    #print('closest:', closest, 'r:', rVal, 'g:', gval, 'b:', bval)
                    #return 'ERROR something went wrong determining the color'

    return colors[closest]