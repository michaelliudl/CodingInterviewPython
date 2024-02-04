from typing import List

class Solution:
    def calculate(self, s: str) -> int:

        def math():
            if operatorSt and operatorSt[-1] in {'+','-'} and len(operandSt) > 1:
                operator = operatorSt.pop()
                operand2 = operandSt.pop()
                operand1 = operandSt.pop()
                if operator == '+': operandSt.append(operand1 + operand2)
                elif operator == '-': operandSt.append(operand1 + operand2)     # Operand was added as negative for -
        
        def combineOperand():
            nonlocal operandLen
            n = operandLen
            operandLen = 0
            if not operandSt or n <= 1 or len(operandSt) < n: 
                return
            operand = 0
            for i in range(n):
                last = operandSt.pop()
                operand += last * (10 ** i)
            operandSt.append(operand)

        if not s: return 0
        operatorSt, operandSt = [],[]
        leftParen, operandLen, addZero = 0, 0, True
        for c in s:
            if c==' ': continue
            if c=='-' and addZero:              # Add 0 if starts with - and has - immediately after (
                operandSt.append(0)
                addZero = False
            if c>='0' and c<='9':
                if operatorSt and operatorSt[-1] == '-':        # Convert + to - negative operand since inside () it needs to be calculated from left to right
                    operandSt.append(-int(c))
                else:
                    operandSt.append(int(c))
                operandLen += 1                 # Keep track of multi digits operands
                addZero = False
            if c in {'+','-','(',')'}:
                combineOperand()                # Combine multi digits into one operand when sees operator
                if c == '(':
                    leftParen += 1              # Keep track of (
                    addZero = True
                if leftParen == 0:
                    math()
                operatorSt.append(c)
                if operatorSt and operatorSt[-1]==')':      # Calculate range of () when meets )
                    while operatorSt:
                        if operatorSt[-1] in {'+', '-'}:
                            math()
                        else:
                            operator = operatorSt.pop()
                            if operator == '(': 
                                leftParen -= 1
                                if operatorSt and operatorSt[-1] == '-' and operandSt:    # Inverse last operand from calculation result from inside() if next operator is also -
                                    operandSt[-1] = -operandSt[-1]
                                break
        combineOperand()
        math()
        return operandSt[0]
                

import unittest

class TestSolution(unittest.TestCase):
    def testCalculate(self):
        s = Solution()
        self.assertEqual(s.calculate(s = "(8+4-(1)+8-10)"), 9)
        self.assertEqual(s.calculate(s = "2-4-(8+2-6+(8+4-(1)+8-10))"), -15)
        self.assertEqual(s.calculate(s = "2-(5-6)"), 3)
        self.assertEqual(s.calculate(s = "1-11"), -10)
        self.assertEqual(s.calculate(s = "1-(     -2)"), 3)
        self.assertEqual(s.calculate(s = "(1+(4+5+2)-3)+(6+8)"), 23)
        self.assertEqual(s.calculate(s = "1 + 1"), 2)
        self.assertEqual(s.calculate(s = " 2-1 + 2 "), 3)
        self.assertEqual(s.calculate(s = "2147483647"), 2147483647)



if __name__ == '__main__':
    unittest.main()