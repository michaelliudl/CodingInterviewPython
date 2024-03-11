from typing import List

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxFreq = 0
        map = {}
        for num in nums:
            map[num] = map.get(num, 0) + 1
            maxFreq = max(maxFreq, map[num])
        ans = 0
        for _, v in map.items():
            ans += maxFreq if v == maxFreq else 0
        return ans

import unittest

class TestSolution(unittest.TestCase):
    def testFindErrorNums(self):
        s = Solution()
        self.assertEqual(s.findErrorNums(nums = [1,2,2,4]), [2,3])
        self.assertEqual(s.findErrorNums(nums = [1,1]), [1,2])
        self.assertEqual(s.findErrorNums(nums = [2,2]), [2,1])
        


if __name__ == '__main__':
    unittest.main()