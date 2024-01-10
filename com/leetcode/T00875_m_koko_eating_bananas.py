from typing import List

class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if not piles or h<=0:
            return 0

    def minEatingSpeedBrute(self, piles: List[int], h: int) -> int:
        if not piles or h<=0:
            return 0
        i=1
        while True:
            t=sum([e//i if e%i==0 else e//i+1 for e in piles])
            if t<=h:
                return i
            i+=1


import unittest

class TestSolution(unittest.TestCase):
    def testMinEatingSpeed(self):
        s = Solution()
        self.assertEqual(s.minEatingSpeed(piles = [3,6,7,11], h = 8), 4)
        self.assertEqual(s.minEatingSpeed(piles = [30,11,23,4,20], h = 5), 30)
        self.assertEqual(s.minEatingSpeed(piles = [30,11,23,4,20], h = 6), 23)



if __name__ == '__main__':
    unittest.main()