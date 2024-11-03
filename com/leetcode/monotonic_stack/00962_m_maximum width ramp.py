from typing import List
from typing import Deque


class Solution:

    # Mono stack to keep index of elements <= stack top element
    # Traverse backwards to get width between current element and element at stack top index
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        n = len(nums)
        for i in range(n):
            num = nums[i]
            if not stack or num <= nums[stack[-1]]:
                stack.append(i)
        res = 0
        for i in range(n - 1, -1, -1):
            num = nums[i]
            while stack and num >= nums[stack[-1]]:
                top = stack.pop()
                res = max(res, (i - top))
        return res

import unittest

class TestSolution(unittest.TestCase):
    def testRemoveKdigits(self):
        s = Solution()
        self.assertEqual(s.removeKdigits(num = "10001", k = 1), '0')
        self.assertEqual(s.removeKdigits(num = "1432219", k = 3), '1219')
        self.assertEqual(s.removeKdigits(num = "10200", k = 1), '200')
        self.assertEqual(s.removeKdigits(num = "10", k = 2), '0')
        self.assertEqual(s.removeKdigits(num = "112", k = 1), '11')



if __name__ == '__main__':
    unittest.main()