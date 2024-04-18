from typing import List

class Solution:

    def addOperators(self, num: str, target: int) -> List[str]:
        
        def backtrack(index, prevOperand, curValue, path):
            if index == len(num):
                if curValue == target:
                    result.append(''.join(path))
                return
            for i in range(index, len(num)):
                if i > index and num[index] == '0':
                    break
                operandStr = num[index:i + 1]
                operandInt = int(operandStr)
                if index == 0:
                    path.append(operandStr)
                    backtrack(i + 1, operandInt, operandInt, path)
                    path.pop()
                else:
                    for operator in ('+', '-', '*'):
                        path.append(operator + operandStr)
                        if operator == '+':
                            backtrack(i + 1, operandInt, curValue + operandInt, path)
                        elif operator == '-':
                            # Convert minus to plus negative operand
                            backtrack(i + 1, -operandInt, curValue - operandInt, path)
                        elif operator == '*':
                            # Convert `a+b*c` where prevOperand is `b` and curValue is a+b
                            # to ((a+b-b) + (b*c)) to handle operator priority
                            backtrack(i + 1, prevOperand * operandInt, (curValue - prevOperand + prevOperand * operandInt), path)
                        path.pop()

        if not num:
            return []
        result = []
        # `prevOperand` is last number in the composed formula
        # `curValue` keeps track of the result of evaluation of the formula
        backtrack(index = 0, prevOperand = 0, curValue = 0, path = [])
        return result




import unittest

class TestSolution(unittest.TestCase):
    def testAddOperators(self):
        s = Solution()
        self.assertEqual(s.addOperators(num = "1111", target = -1), ["1-1-1*1","1-1*1-1","1*1-1-1"])
        self.assertEqual(s.addOperators(num = "00", target = 0), ["0+0","0-0","0*0"])
        self.assertEqual(s.addOperators(num = "123", target = 6), ["1+2+3","1*2*3"])
        self.assertEqual(s.addOperators(num = "232", target = 8), ["2+3*2","2*3+2"])
        self.assertEqual(s.addOperators(num = "3456237490", target = 9191), [])


if __name__ == '__main__':
    unittest.main()