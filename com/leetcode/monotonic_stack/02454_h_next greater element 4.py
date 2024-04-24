from typing import List
import heapq

class Solution:

    # Use first mono desc stack to hold elements with 0 next greater
    # Use second mono desc stack to hold elements with 1 next greater
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums
        n = len(nums)
        res = [-1] * n
        stack = []
        stackOfOneGreater = []
        for i in range(n):
            num = nums[i]
            # See second next greater
            while stackOfOneGreater and num > nums[stackOfOneGreater[-1]]:
                res[stackOfOneGreater.pop()] = num
            temp = []
            # See first next greater, move to second stack
            while stack and num > nums[stack[-1]]:
                temp.append(stack.pop())
            while temp:
                stackOfOneGreater.append(temp.pop())
            stack.append(i)
        return res

import unittest

class TestSolution(unittest.TestCase):
    def testSumSubarrayMins(self):
        s = Solution()
        self.assertEqual(s.sumSubarrayMins(arr = [3,1,2,4]), 17)
        self.assertEqual(s.sumSubarrayMins(arr = [11,81,94,43,3]), 444)
        


if __name__ == '__main__':
    unittest.main()