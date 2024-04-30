from typing import List
import math

class Solution:

    def maximumPrimeDifference(self, nums: List[int]) -> int:

        def prime(num):
            if num < 2:
                return False
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    return False
            return True

        if not nums:
            return 0
        n = len(nums)
        first, last = -1, n
        for i in range(n):
            if first < 0 and prime(nums[i]):
                first = i
            if last == n and prime(nums[n - 1 - i]):
                last = n - 1 - i
            if 0 <= first <= last < n:
                break
        return last - first



import unittest

class TestSolution(unittest.TestCase):
    def testbulbSwitch(self):
        s = Solution()
        self.assertEqual(s.bulbSwitch(3), 1)
        self.assertEqual(s.bulbSwitch(0), 0)
        self.assertEqual(s.bulbSwitch(1), 1)


if __name__ == '__main__':
    unittest.main()