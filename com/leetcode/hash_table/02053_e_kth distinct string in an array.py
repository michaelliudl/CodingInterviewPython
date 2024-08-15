from typing import List, Counter

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counts = Counter(arr)
        count = 0
        for string in arr:
            if counts[string] == 1:
                count += 1
                if count == k:
                    return string
        return ''

import unittest

class TestSolution(unittest.TestCase):
    def testFindErrorNums(self):
        s = Solution()
        self.assertEqual(s.findErrorNums(nums = [1,2,2,4]), [2,3])
        self.assertEqual(s.findErrorNums(nums = [1,1]), [1,2])
        self.assertEqual(s.findErrorNums(nums = [2,2]), [2,1])
        


if __name__ == '__main__':
    unittest.main()