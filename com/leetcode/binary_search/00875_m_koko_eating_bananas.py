from typing import List

class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if not piles or h<len(piles):
            return 0
        b,e=1,max(piles)
        while b<e:
            mid=(b+e)//2
            total=sum([e//mid if e%mid==0 else e//mid+1 for e in piles])
            if total<=h:
                e=mid
            else:
                b=mid+1
        return b

import unittest

class TestSolution(unittest.TestCase):
    def testMinEatingSpeed(self):
        s = Solution()
        self.assertEqual(s.minEatingSpeed(piles = [3,6,7,11], h = 8), 4)
        self.assertEqual(s.minEatingSpeed(piles = [30,11,23,4,20], h = 5), 30)
        self.assertEqual(s.minEatingSpeed(piles = [30,11,23,4,20], h = 6), 23)



if __name__ == '__main__':
    unittest.main()