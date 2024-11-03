from typing import List
from typing import Deque
from functools import cmp_to_key

class Solution:

    # Sort then check if later string is substring
    def removeSubfolders(self, folder: list[str]) -> list[str]:
        folder.sort()
        prefix = ''
        res = []
        for fold in folder:
            if prefix and fold.startswith(prefix) and fold[len(prefix)] == '/':
                continue
            res.append(fold)
            prefix = fold
        return res


import unittest

class TestSolution(unittest.TestCase):
    def testCarFleet(self):
        s = Solution()
        self.assertEqual(s.carFleet(target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]), 3)
        self.assertEqual(s.carFleet(target = 10, position = [3], speed = [3]), 1)
        self.assertEqual(s.carFleet(target = 100, position = [0,2,4], speed = [4,2,1]), 1)



if __name__ == '__main__':
    unittest.main()