from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        if not nums or len(nums)<2: return nums
        ans = []
        positive, negative = [], []
        for num in nums:
            if num > 0:
                positive.append(num)
            else:
                negative.append(num)
        for i in range(len(positive)):
            ans.append(positive[i])
            ans.append(negative[i])
        return ans


import unittest

class TestSolution(unittest.TestCase):
    def testRearrangeArray(self):
        s = Solution()
        self.assertEqual(s.rearrangeArray(nums = [3,1,-2,-5,2,-4]), [3,-2,1,-5,2,-4])
        self.assertEqual(s.rearrangeArray(nums = [-1,1]), [1,-1])

if __name__ == '__main__':
    unittest.main()