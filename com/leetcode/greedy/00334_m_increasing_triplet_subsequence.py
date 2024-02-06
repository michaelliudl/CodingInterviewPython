from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if not nums or len(nums)<3: return False
        first, second = float('inf'), float('inf')
        for num in nums:
            if num<=first:
                first=num
            elif num<=second:
                second=num
            else:
                return True
        return False


import unittest

class TestSolution(unittest.TestCase):
    def testIncreasingTriplet(self):
        s = Solution()
        self.assertEqual(s.increasingTriplet(nums = [2,1,5,0,6,7]), True)
        self.assertEqual(s.increasingTriplet(nums = [1,2,3,4,5]), True)
        self.assertEqual(s.increasingTriplet(nums = [5,4,3,2,1]), False)


if __name__ == '__main__':
    unittest.main()