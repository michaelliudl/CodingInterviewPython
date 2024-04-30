from typing import List

class Solution:

    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        # Sum and count # of zeros
        sum1 = sum(nums1)
        zeros1 = sum(1 for num in nums1 if num == 0)
        sum2 = sum(nums2)
        zeros2 = sum(1 for num in nums2 if num == 0)

        # If one array has no zero and it's sum is smaller than the sum of the other array plus number of zeros, there is no way to equal
        if zeros1 == 0 and sum1 < sum2 + zeros2:
            return -1
        if zeros2 == 0 and sum2 < sum1 + zeros1:
            return -1
        return max(sum1 + zeros1, sum2 + zeros2)



import unittest

class TestSolution(unittest.TestCase):
    def testbulbSwitch(self):
        s = Solution()
        self.assertEqual(s.bulbSwitch(3), 1)
        self.assertEqual(s.bulbSwitch(0), 0)
        self.assertEqual(s.bulbSwitch(1), 1)


if __name__ == '__main__':
    unittest.main()