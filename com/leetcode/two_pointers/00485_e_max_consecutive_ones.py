from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if not nums:
            return 0
        left = ans = 0
        for right in range(len(nums)):
            if nums[right] == 1:
                while nums[left] == 0:
                    left += 1
                ans = max(ans, (right - left + 1))
            else:
                left = right
        return ans

import unittest

class TestSolution(unittest.TestCase):
    def testIsPalindrome(self):
        s = Solution()
        self.assertEqual(s.findMaxConsecutiveOnes(nums = [1,1,0,1,1,1]), 3)
        self.assertEqual(s.findMaxConsecutiveOnes(nums = [1,0,1,1,0,1]), 2)


if __name__ == '__main__':
    unittest.main()