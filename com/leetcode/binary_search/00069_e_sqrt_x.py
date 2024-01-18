from typing import List

class Solution:
    def mySqrt(self, x: int) -> int:
        if x<=1:
            return x
        low,high=1,x
        while low<=high:
            mid=low+(high-low)//2
            p=mid*mid
            if p==x:
                return mid
            elif p>x:
                high=mid-1
            else:
                low=mid+1
        return high


import unittest

class TestSolution(unittest.TestCase):
    def testTwoSum(self):
        s = Solution()
        self.assertEqual(s.twoSum([2,7,11,15],9), [0,1])
        self.assertEqual(s.twoSum([3,2,4],6), [1,2])
        self.assertEqual(s.twoSum([3,3],6), [0,1])


if __name__ == '__main__':
    unittest.main()