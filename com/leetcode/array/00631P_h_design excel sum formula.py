from typing import List

'''
Design the basic function of Excel and implement the function of the sum formula.

Implement the Excel class:

Excel(int height, char width) Initializes the object with the height and the width of the sheet. The sheet is an integer matrix mat of size height x width with the row index in the range [1, height] and the column index in the range ['A', width]. All the values should be zero initially.
void set(int row, char column, int val) Changes the value at mat[row][column] to be val.
int get(int row, char column) Returns the value at mat[row][column].
int sum(int row, char column, List<String> numbers) Sets the value at mat[row][column] to be the sum of cells represented by numbers and returns the value at mat[row][column]. This sum formula should exist until this cell is overlapped by another value or another sum formula. numbers[i] could be on the format:
"ColRow" that represents a single cell.
For example, "F7" represents the cell mat[7]['F'].
"ColRow1:ColRow2" that represents a range of cells. The range will always be a rectangle where "ColRow1" represent the position of the top-left cell, and "ColRow2" represents the position of the bottom-right cell.
For example, "B3:F7" represents the cells mat[i][j] for 3 <= i <= 7 and 'B' <= j <= 'F'.
Note: You could assume that there will not be any circular sum reference.

For example, mat[1]['A'] == sum(1, "B") and mat[1]['B'] == sum(1, "A").

'''

class Excel:

    def __init__(self, height: int, width: str):
        self.grid = [[0] * (ord(width) - ord('A') + 2) for _ in range(height + 1)]
        self.cellValue = {}
        self.cellFormula = {}
        self.cellUpdate = {}
    
    def set(self, row: int, column: str, val: int) -> None:
        col = ord(column) - ord('A') + 1
        oldVal = self.getInternal(row, col)
        self.grid[row][col] = val
        # If prev is formula
        self.handlePrevFormula(row, col)
        # Recur recalculate impacted cells
        self.recurCalc(row, col, oldVal, val)

    def get(self, row: int, column: str) -> int:
        col = ord(column) - ord('A') + 1
        return self.getInternal(row, col)

    def sum(self, row: int, column: str, numbers: List[str]) -> int:
        col = ord(column) - ord('A') + 1
        oldVal = self.getInternal(row, col)
        self.grid[row][col] = 0
        # If prev is formula
        self.handlePrevFormula(row, col)
        # Calc new formula and add affecting cells
        self.calcNewFormula(row, col, numbers)
        # Recur recalculate impacted cells
        newVal = self.cellValue[(row, col)]
        self.recurCalc(row, col, oldVal, newVal)
        return newVal

    def calcNewFormula(self, row: int, col: int, numbers: List[str]):
        self.cellFormula[(row, col)] = numbers
        result, fromCells = self.parseFormula(numbers)
        for fromRow, fromCol in fromCells:
            if (fromRow, fromCol) not in self.cellUpdate:
                self.cellUpdate[(fromRow, fromCol)] = []
            self.cellUpdate[(fromRow, fromCol)].append((row, col))
        self.cellValue[(row, col)] = result

    def recurCalc(self, row: int, col: int, oldVal: int, val: int):
        if (row, col) not in self.cellUpdate:
            return
        for rowA, colA in self.cellUpdate[(row, col)]:
            oldA = self.getInternal(rowA, colA)
            newA = oldA + (val - oldVal)
            self.updateVal(rowA, colA, newA)
            self.recurCalc(rowA, colA, oldA, newA)
    
    def updateVal(self, row: int, col: int, val: int):
        if (row, col) in self.cellValue:
            self.cellValue[(row, col)] = val
        else:
            self.grid[row][col] = val

    def handlePrevFormula(self, row:int, col:int):
        if (row, col) in self.cellValue:
            del self.cellValue[(row, col)]
        if (row, col) in self.cellFormula:
            _, fromCells = self.parseFormula(self.cellFormula[(row, col)])
            for fromCell in fromCells:
                if (row, col) in self.cellUpdate[fromCell]:
                    self.cellUpdate[fromCell].remove((row, col))
                if not self.cellUpdate[fromCell]:
                    del self.cellUpdate[fromCell]
            del self.cellFormula[(row, col)]

    def parseFormula(self, numbers: List[str]):
        def getRC(cellStr):
            row = int(cellStr[1:])
            col = ord(cellStr[0]) - ord('A') + 1
            return (row, col)

        result = 0
        fromCells = []
        for formula in numbers:
            formList = formula.split(':')
            if len(formList) == 1:
                r, c = getRC(formList[0])
                result += self.getInternal(r, c)
                fromCells.append((r, c))
            else:
                rTop, cLeft = getRC(formList[0])
                rBot, cRight = getRC(formList[1])
                for i in range(rTop, rBot + 1):
                    for j in range(cLeft, cRight + 1):
                        result += self.getInternal(i, j)
                        fromCells.append((i, j))
        return (result, fromCells)
    
    def getInternal(self, row:int, col:int) -> int:
        if (row, col) in self.cellValue:
            return self.cellValue[(row, col)]
        return self.grid[row][col]

# Your Excel object will be instantiated and called as such:
# obj = Excel(height, width)
# obj.set(row,column,val)
# param_2 = obj.get(row,column)
# param_3 = obj.sum(row,column,numbers)

class Solution:
    pass

import unittest

class TestSolution(unittest.TestCase):

    def testExcel(self):
        e = Excel(height=5, width='E')
        e.set(row=1, column='A', val=1)
        result = e.sum(row=2, column='B', numbers=["A1"])
        self.assertEqual(result, 1)
        e.set(row=2, column='B', val=0)
        result = e.get(row=2, column='B')
        self.assertEqual(result, 0)
        e.set(row=1, column='A', val=5)
        result = e.get(row=2, column='B')
        self.assertEqual(result, 0)

    # def testExcel2(self):
    #     e = Excel(height=5, width='E')
    #     result = e.get(row=1, column='A')
    #     self.assertEqual(result, 0)
    #     e.set(row=1, column='A', val=1)
    #     result = e.get(row=1, column='A')
    #     self.assertEqual(result, 1)
    #     result = e.sum(row=2, column='B', numbers=["A1", "A1"])
    #     self.assertEqual(result, 2)
    #     e.set(row=1, column='A', val=2)
    #     result = e.get(row=2, column='B')
    #     self.assertEqual(result, 4)

    # def testExcel1(self):
    #     e = Excel(height=3, width='C')
    #     e.set(row=1, column='A', val=2)
    #     result = e.sum(row=3, column='C', numbers=["A1", "A1:B2"])
    #     self.assertEqual(result, 4)
    #     e.set(row=2, column='B', val=2)
    #     result = e.get(row=3, column='C')
    #     self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()