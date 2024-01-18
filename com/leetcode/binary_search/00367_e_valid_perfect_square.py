from typing import List

class Solution:
    
    def isPerfectSquare(self, num: int) -> bool:
        if num<0:
            return False
        low,high=0,num
        while low<=high:
            mid=low+(high-low)//2
            sq=mid*mid
            if sq>num:
                high=mid-1
            elif sq<num:
                low=mid+1
            else:
                return True
        return False


import unittest

class TestSolution(unittest.TestCase):
    def testTwoSum(self):
        s = Solution()
        self.assertEqual(s.twoSum([2,7,11,15],9), [0,1])
        self.assertEqual(s.twoSum([3,2,4],6), [1,2])
        self.assertEqual(s.twoSum([3,3],6), [0,1])


if __name__ == '__main__':
    unittest.main()