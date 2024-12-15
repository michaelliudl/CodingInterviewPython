from typing import List, Counter

class Solution:

    # Check case of number of 0s
    def checkIfExist(self, arr: List[int]) -> bool:
        counts = Counter(arr)
        if 0 in counts and counts[0] > 1:
            return True
        for num, _ in counts.items():
            if num != 0 and (num * 2) in counts:
                return True
        return False

import unittest

class TestSolution(unittest.TestCase):
    def testTwoSum(self):
        s = Solution()
        self.assertEqual(s.twoSum([2,7,11,15],9), [0,1])
        self.assertEqual(s.twoSum([3,2,4],6), [1,2])
        self.assertEqual(s.twoSum([3,3],6), [0,1])


if __name__ == '__main__':
    unittest.main()