from typing import List

class Solution:

    # For each location, scan forward to get force from left to right
    # Scan backwards to get force from right to left
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        forces = [0] * n
        force = 0
        for i in range(n):
            if dominoes[i] == 'R':
                force = n
            elif dominoes[i] == 'L':
                force = 0
            else:
                force = max(force - 1, 0)
            forces[i] = force
        force = 0
        for i in range(n - 1, -1, -1):
            if dominoes[i] == 'L':
                force = n
            elif dominoes[i] == 'R':
                force = 0
            else:
                force = max(force - 1, 0)
            forces[i] -= force              # Net force left to right and right to left
        return ''.join('.' if f == 0 else 'R' if f > 0 else 'L' for f in forces)

import unittest

class TestSolution(unittest.TestCase):

    def testCompress(self):
        s = Solution()
        chars = ["a","a","b","b","c","c","c"]
        self.assertEqual(s.compress(chars), 6)
        self.assertEqual(chars[:6], ["a","2","b","2","c","3"])
        chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
        self.assertEqual(s.compress(chars), 4)
        self.assertEqual(chars[:4], ["a","b","1","2"])

if __name__ == '__main__':
    unittest.main()