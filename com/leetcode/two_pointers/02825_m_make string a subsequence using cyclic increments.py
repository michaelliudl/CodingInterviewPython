from typing import List

class Solution:
    
    # Use two pointers on both strings to check if the operation is possible
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i = 0   # Index in `str2`
        for char in str1:   # Check if `str2` is formed by characters or 1 off characters in `str1`
            if char == str2[i] or (ord(str2[i]) == (ord('a') + (ord(char) - ord('a') + 1) % 26)):
                i += 1
                if i == len(str2):
                    return True
        return False

import unittest

class TestSolution(unittest.TestCase):
    def testCanChange(self):
        s = Solution()
        self.assertEqual(s.canChange(start = "_L__R__R_", target = "L______RR"), True)
        self.assertEqual(s.canChange(start = "R_L_", target = "__LR"), False)
        self.assertEqual(s.canChange(start = "_R", target = "R_"), False)
        self.assertEqual(s.canChange(start = "_L__R__R_L", target = "L______RR_"), False)


if __name__ == '__main__':
    unittest.main()