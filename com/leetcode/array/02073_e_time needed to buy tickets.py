from typing import List

class Solution:

    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        result = 0
        while True:
            for i in range(len(tickets)):
                if tickets[i] > 0:
                    tickets[i] -= 1
                    result += 1
                if i == k and tickets[i] == 0:
                    return result
        

import unittest

class TestSolution(unittest.TestCase):

    def testPivotIndex(self):
        s=Solution()
        self.assertEqual(s.pivotIndex(nums = [1,7,3,6,5,6]), 3)
        self.assertEqual(s.pivotIndex(nums = [2,1,-1]), 0)
        self.assertEqual(s.pivotIndex(nums = [1,2,3]), -1)

if __name__ == '__main__':
    unittest.main()