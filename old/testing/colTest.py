# ===> Imports & Libraries
import sys
import random
# ===> Constants & Global Variables
# <Variable description>
sys.path.insert(0, '../modules')
from input import *


# ===> Functions & Classes
# <Function description>
RGBColorVals = [
    (255, 255, 255),
    (0, 0, 0),
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 255, 0),
    (255, 0, 255),
    (0, 255, 255),
    (128, 0, 0),
    (0, 128, 0),
    (0, 0, 128),
    (128, 128, 0),
    (128, 0, 128),
    (0, 128, 128),
    (192, 192, 192),
    (128, 128, 128),
]


# ===> Main Function
# <main -> <your description>
def main():
    for i in range(0, 10):
        colVal = random.choice(RGBColorVals)
        getCol(colVal[0], colVal[1], colVal[2], 1)
    pass
    
# ===> Execute Main Function
if __name__ == '__main__':
    main()
