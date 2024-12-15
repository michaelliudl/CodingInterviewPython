from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        if not height: return 0
        ans, left, right = 0, 0, len(height) - 1
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            ans = max(ans, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans


import unittest

class TestSolution(unittest.TestCase):
    def testMaxArea(self):
        s = Solution()
        self.assertEqual(s.maxArea(height = [1,8,6,2,5,4,8,3,7]), 49)
        self.assertEqual(s.maxArea(height = [1,1]), 1)


if __name__ == '__main__':
    unittest.main()