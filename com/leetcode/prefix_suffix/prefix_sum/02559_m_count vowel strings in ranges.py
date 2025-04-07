from typing import List

class Solution:

    # Use prefix sum to count number of words starting and ending with vowels
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set('aeiou')
        prefixSum = [0] * (len(words) + 1)
        for i, word in enumerate(words):
            prefixSum[i + 1] = prefixSum[i] + (1 if (word[0] in vowels and word[-1]) in vowels else 0)
        return [(prefixSum[end + 1] - prefixSum[start]) for start, end in queries]

import unittest

class TestSolution(unittest.TestCase):
    def testCheckSubarraySum(self):
        s = Solution()
        self.assertEqual(s.checkSubarraySum(nums = [5,0,0,0], k = 3), True)
        self.assertEqual(s.checkSubarraySum(nums = [0,1,0,3,0,4,0,4,0], k = 5), False)
        self.assertEqual(s.checkSubarraySum(nums = [23,2,4,6,7], k = 6), True)
        self.assertEqual(s.checkSubarraySum(nums = [23,2,6,4,7], k = 6), True)
        self.assertEqual(s.checkSubarraySum(nums = [23,2,6,4,7], k = 13), False)


if __name__ == '__main__':
    unittest.main()