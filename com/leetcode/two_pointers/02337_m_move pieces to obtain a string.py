from typing import List

class Solution:
    
    # Use two pointers on both strings to check if moving is possible
    def canChange(self, start: str, target: str) -> bool:
        n = len(start)
        i = j = 0
        while i <= n and j <= n:
            while i < n and start[i] == '_':
                i += 1
            while j < n and target[j] == '_':
                j += 1
            if i == n or j == n:        # If one pointer reaches the end, return `True` if both pointers reach the end
                return i == n and j == n
            if start[i] != target[j]:   # `L`s and `R`s should be on the same side in both strings
                return False
            if start[i] == 'R' and i > j:   # `target` has `R`s to the left of the first `R` in `start`
                return False
            if start[i] == 'L' and i < j:   # `target` has `L`s to the right of the first `L` in `start`
                return False
            i += 1  # Move over matching characters
            j += 1
        return True

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