from typing import List, Counter

class Solution:

    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        pairSum = sum(skill) // (n // 2)    # Sum value of all pairs
        counts = Counter(skill)
        res = 0
        for num, numCount in counts.items():
            diff = pairSum - num
            if counts[diff] != numCount:    # Not same count of numbers that sums to pair sum
                return -1
            res += (num * diff * numCount)  # Sum of products of each pair
        return res // 2     # Pairs considered twice

import unittest

class TestSolution(unittest.TestCase):
    def testGroupAnagrams(self):
        s = Solution()
        # self.assertEqual(s.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]), [["bat"],["nat","tan"],["ate","eat","tea"]])
        self.assertEqual(s.groupAnagrams(strs = ["bdddddddddd","bbbbbbbbbbc"]), [["bbbbbbbbbbc"],["bdddddddddd"]])

if __name__ == '__main__':
    unittest.main()