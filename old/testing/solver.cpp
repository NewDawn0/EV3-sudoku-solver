#include<iostream>
#include<fstream>
#define Size 9

int board[9][9];
void printBoard() {
    for (int line = 0; line < Size; line++) {
        if (line != 0 && line % 3 == 0) {
            std::cout << "------┼-------┼------" << std::endl;
        }
        for (int num = 0; num < 9; num++) {
            if (num != 0 && num % 3 == 0) {
                std::cout << "| ";
            }
            if (num == 8) {
                std::cout << board[line][num] << std::endl;
            } else {
                std::cout << board[line][num] << " ";
            }
        }
    }
}
void input() {
    // Opening the file
    std::ifstream inputfile("io.txt");

    if (!inputfile.is_open())
        std::cout << "Error opening file";

    // Defining the loop for getting input from the file

    for (int r = 0; r < Size; r++)
    {
        for (int c = 0; c < Size; c++)
        {
            inputfile >> board[r][c];
        }
    }
}
bool checkRow(int row, int num) { // check whether num is present in row or not
    for (int col = 0; col < Size; col++)
        if (board[row][col] == num)
            return true;
    return false;
}
bool checkCol(int col, int num) { // check whether num is present in col or not
    for (int row = 0; row < Size; row++)
        if (board[row][col] == num)
            return true;
    return false;
}
bool checkBox(int boxStartRow, int boxStartCol, int num) {
    // check whether num is present in 3x3 box or not
    for (int row = 0; row < 3; row++)
        for (int col = 0; col < 3; col++)
            if (board[row + boxStartRow][col + boxStartCol] == num)
                return true;
    return false;
}
bool getFree(int &row, int &col) { // get empty location and update row and column
    for (row = 0; row < Size; row++)
        for (col = 0; col < Size; col++)
            if (board[row][col] == 0) // marked with 0 is empty
                return true;
    return false;
}
bool getValid(int row, int col, int num) {
    // when item not found in col, row and current 3x3 box
    return !checkRow(row, num) && !checkCol(col, num) && !checkBox(row - row % 3, col - col % 3, num);
}
bool solve() {
    int row, col;
    if (!getFree(row, col)) {
        return true; // when all places are filled
    }
    for (int num = 1; num <= 9; num++) { // valid numbers are 1 - 9
        if (getValid(row, col, num)) { // check validation, if yes, put the number in the grid
            board[row][col] = num;
            if (solve()) { // recursively go for other rooms in the grid
                return true;
            }
            board[row][col] = 0; // turn to unassigned space when conditions are not satisfied
        }
    }
    return false;
}
int main() {
    input();
    std::cout << "Input Board" << std::endl;
    printBoard();
    std::cout << std::endl;
    if (solve()) {
        std::cout << "Solution" << std::endl;
        printBoard();
    } else {
        std::cout << "No solution" << std::endl;
    }
    return 0;
}