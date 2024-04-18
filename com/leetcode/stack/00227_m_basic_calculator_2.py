from typing import List

class Solution:

    def calculate(self, s: str) -> int:
        ans = 0
        prevNum = 0
        currNum = 0
        op = '+'

        for i, c in enumerate(s):
            if c.isdigit():
                currNum = currNum * 10 + int(c)
            if not c.isdigit() and c != ' ' or i == len(s) - 1:
                if op == '+' or op == '-':
                    ans += prevNum
                    prevNum = currNum if op == '+' else -currNum
                elif op == '*':
                    prevNum = prevNum * currNum
                elif op == '/':
                    if prevNum < 0:
                        prevNum = math.ceil(prevNum / currNum)
                    else:
                        prevNum = prevNum // currNum
                op = c
                currNum = 0

        return ans + prevNum

    def calculate(self, s: str) -> int:
        if not s: return 0
        oprSt, opdSt = [], []
        numberFlag = False
        for c in s:
            if c == ' ':
                numberFlag = False
                continue
            if c in ('+', '-', '*', '/'):
                while oprSt and (oprSt[-1] in ('*', '/') or (oprSt[-1] == '-' and c in ('+', '-'))):
                    opr = oprSt.pop()
                    num2 = opdSt.pop()
                    num1 = opdSt.pop()
                    if opr == '*': 
                        opdSt.append(num1 * num2)
                    elif opr == '/':
                        opdSt.append(num1 // num2) 
                    else:
                        opdSt.append(num1 - num2)
                oprSt.append(c)
                numberFlag = False
            else:
                cur = int(c)
                if numberFlag:
                    prev = opdSt.pop()
                    opdSt.append(prev * 10 + cur)
                else:
                    opdSt.append(cur)
                    numberFlag = True
        while oprSt and opdSt:
            opr = oprSt.pop()
            num2 = opdSt.pop()
            num1 = opdSt.pop()
            if opr == '*':
                opdSt.append(num1 * num2)
            elif opr == '/':
                opdSt.append(num1 // num2)
            elif opr == '+':
                opdSt.append(num1 + num2)
            else:
                opdSt.append(num1 - num2)
        return opdSt[0]

import unittest

class TestSolution(unittest.TestCase):
    def testCalculate(self):
        s = Solution()
        self.assertEqual(s.calculate(s = "1*2-3/4+5*6-7*8+9/10"), -24)
        self.assertEqual(s.calculate(s = "1-1+1"), 1)
        self.assertEqual(s.calculate(s = "3+2*2"), 7)
        self.assertEqual(s.calculate(s = " 3/2 "), 1)
        self.assertEqual(s.calculate(s = " 3+5 / 2 "), 5)



if __name__ == '__main__':
    unittest.main()