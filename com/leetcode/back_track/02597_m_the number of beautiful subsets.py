from typing import List, DefaultDict

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:

        def backtrack(index):
            if index == len(nums):
                return 1
            res = backtrack(index + 1)  # Skip nums[index]
            if counts[nums[index] + k] == 0 and counts[nums[index] - k] == 0:
                # Include nums[index]
                counts[nums[index]] += 1
                res += backtrack(index + 1)
                counts[nums[index]] -= 1
            return res

        counts = DefaultDict(int)
        return backtrack(index=0) - 1

import unittest

class TestSolution(unittest.TestCase):
    def testBeautifulSubsets(self):
        s = Solution()
        self.assertEqual(s.beautifulSubsets(nums = [2,4,6], k = 2), 4)
        self.assertEqual(s.beautifulSubsets(nums = [1], k = 1), 1)
        


if __name__ == '__main__':
    unittest.main()