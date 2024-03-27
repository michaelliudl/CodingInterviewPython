from typing import List,Optional

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if not nums:
            return 0
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            if counts[num] > 1:
                return num
        return 0

import unittest

class TestSolution(unittest.TestCase):
    def testHasCycle(self):
        s = Solution()
        self.assertEqual(s.hasCycle(ListNode(1,ListNode(2,None))), False)


if __name__ == '__main__':
    unittest.main()