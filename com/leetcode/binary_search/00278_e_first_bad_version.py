from typing import List

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:

    def firstBadVersion(self, n: int) -> int:

        def isBadVersion(version: int) -> bool:
            pass

        low,high=1,n
        while low<high:
            mid=low+(high-low)//2
            if isBadVersion(mid):
                high=mid
            else:
                low=mid+1
        return low

    def firstBadVersion_1(self, n: int) -> int:
        def isBadVersion(version: int) -> bool:
            return version==2

        if n<=0: return n
        if isBadVersion(1): return 1
        low,high=1,n
        while low<high:
            mid=low+(high-low)//2
            if isBadVersion(mid):
                high=mid if high>mid else mid-1
            else:
                low=mid if low<mid else mid+1
        return low

import unittest

class TestSolution(unittest.TestCase):
    def testFirstBadVersion(self):
        s = Solution()
        # self.assertEqual(s.firstBadVersion(5), 4)
        self.assertEqual(s.firstBadVersion(3), 2)
        

if __name__ == '__main__':
    unittest.main()