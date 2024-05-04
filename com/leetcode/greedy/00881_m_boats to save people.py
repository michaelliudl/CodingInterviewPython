from typing import List

class Solution:

    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        low, high = 0, len(people) - 1
        res = 0
        while low <= high:
            if people[high] > limit:
                return -1
            if low == high:
                res += 1
                break
            if people[high] + people[low] <= limit:
                high -= 1
                low += 1
            else:
                high -= 1
            res += 1
        return res

import unittest

class TestSolution(unittest.TestCase):
    def testPartitionLabels(self):
        s = Solution()
        self.assertEqual(s.partitionLabels(s = "ababcbacadefegdehijhklij"), [9,7,8])
        self.assertEqual(s.partitionLabels(s = "eccbbbbdec"), [10])
        self.assertEqual(s.partitionLabels(s = "caedbdedda"), [1,9])
        


if __name__ == '__main__':
    unittest.main()