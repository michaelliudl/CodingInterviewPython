from typing import List

class Solution:

    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        if not nums: return 0
        nums.sort()
        minAfter,kAfter=0,k
        for i in range(len(nums)):
            if nums[i]<0 and kAfter>0:
                nums[i] = -nums[i]
                kAfter-=1
                minAfter+=1
            else:
                break
        if minAfter>0:
            if minAfter==len(nums):
                minAfter=len(nums)-1
            elif nums[minAfter] > nums[minAfter-1]:
                minAfter-=1
        for i in range(kAfter):
            nums[minAfter] = -nums[minAfter]
        return sum(nums)
        




import unittest

class TestSolution(unittest.TestCase):
    def testLargestSumAfterKNegations(self):
        s = Solution()
        self.assertEqual(s.largestSumAfterKNegations(nums = [4,2,3], k = 1), 5)
        self.assertEqual(s.largestSumAfterKNegations(nums = [3,-1,0,2], k = 3), 6)
        self.assertEqual(s.largestSumAfterKNegations(nums = [2,-3,-1,5,-4], k = 2), 13)
        self.assertEqual(s.largestSumAfterKNegations(nums = [-2,9,9,8,4], k = 5), 32)
        self.assertEqual(s.largestSumAfterKNegations(nums = [-4,-2,-3], k = 4), 5)
        


if __name__ == '__main__':
    unittest.main()