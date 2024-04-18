from typing import List
from typing import Deque


class Solution:

    # Similar to 84, use Monotonic stack to track index of increasing elements
    # Calculate when next element in array is smaller than number on index of stack's top
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        if not nums:
            return 0
        # First dummy `0` for popping first element of array case
        # Last dummy `0` for forcing to pop all array elements out of the stack
        nums = [0] + nums + [0]   # Add dummy elements to front for getting start index, and to back for all ascending case
        stack = []             # Stack holds index
        for i, num in enumerate(nums):
            while stack and num < nums[stack[-1]]:  # Pop top and calcualte when current element is smaller than array element at top index
                midIndex = stack.pop()
                height = nums[midIndex]     # Height of rectangle like in 84, it's smallest element in current subarray
                leftIndex = stack[-1]
                width = (i - leftIndex - 1) # Width of rectangle like in 84
                if height * width > threshold:  # All elements are greater than threshold / k means ((min element in subarray) * k > threshold), k is length of subarray
                    return width
            stack.append(i)
        return -1



import unittest

class TestSolution(unittest.TestCase):
    def testLargestRectangleArea(self):
        s = Solution()
        self.assertEqual(s.largestRectangleArea(heights = [2,1,5,6,2,3]), 10)
        self.assertEqual(s.largestRectangleArea(heights = [2,4]), 4)



if __name__ == '__main__':
    unittest.main()