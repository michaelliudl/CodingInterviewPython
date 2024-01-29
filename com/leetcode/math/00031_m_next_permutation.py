from typing import List

class Solution:

    # Loop backwards and find first index i that nums[i]>nums[i-1]
    # Loop backwards and find first index j that nums[j]>nums[i-1] and swap
    # Swap in pairs from i to end
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums: return
        n=len(nums)
        rightPeak=n-1
        while rightPeak>0 and nums[rightPeak]<=nums[rightPeak-1]:
            rightPeak-=1
        if rightPeak>0:
            for i in range(n-1,rightPeak-1,-1):
                if nums[i]>nums[rightPeak-1]:
                    nums[i],nums[rightPeak-1]=nums[rightPeak-1],nums[i]
                    break
        low,high=rightPeak,n-1
        while low<high:
            nums[low],nums[high]=nums[high],nums[low]
            low+=1
            high-=1



import unittest

class TestSolution(unittest.TestCase):
    def testbulbSwitch(self):
        s = Solution()
        self.assertEqual(s.bulbSwitch(3), 1)
        self.assertEqual(s.bulbSwitch(0), 0)
        self.assertEqual(s.bulbSwitch(1), 1)


if __name__ == '__main__':
    unittest.main()