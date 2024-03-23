from typing import List

class Solution:
    def isStrobogrammatic(self, num: str) -> bool:

        def strobo(num1, num2):
            return (num1 == num2 and num1 in (0,1,8)) or (num1 == 6 and num2 == 9) or (num1 == 9 and num2 == 6)

        if not num:
            return False
        low, high = 0, len(num) - 1
        while low <= high:
            if not strobo(int(num[low]), int(num[high])):
                return False
            low += 1
            high -= 1
        return True
    
import unittest

class TestSolution(unittest.TestCase):
    def testIsStrobogrammatic(self):
        s = Solution()
        self.assertEqual(s.isStrobogrammatic(num = "69"), True)
        self.assertEqual(s.isStrobogrammatic(num = "88"), True)
        self.assertEqual(s.isStrobogrammatic(num = "962"), False)


if __name__ == '__main__':
    unittest.main()
