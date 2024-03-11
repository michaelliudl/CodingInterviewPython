from typing import List

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        if not nums or k <= 0:
            return []


import unittest

class TestSolution(unittest.TestCase):
    def testMaxSumOfThreeSubarrays(self):
        s = Solution()
        self.assertEqual(s.maxSumOfThreeSubarrays("/home/"), "/home")
        self.assertEqual(s.maxSumOfThreeSubarrays("/../"), "/")
        self.assertEqual(s.maxSumOfThreeSubarrays("/home//foo/"), "/home/foo")



if __name__ == '__main__':
    unittest.main()