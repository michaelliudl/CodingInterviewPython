from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        nums.sort()
        closeSum, closeDiff = 0, float('inf')
        for left in range(len(nums) - 2):
            mid, right = left + 1, len(nums) - 1
            while mid < right:
                curSum = nums[left] + nums[mid] + nums[right]
                diff = abs(curSum - target)
                if diff == 0:
                    return curSum
                if diff < closeDiff:
                    closeDiff = diff
                    closeSum = curSum
                if curSum < target:
                    mid += 1
                else:
                    right -= 1
        return closeSum



import unittest

class TestSolution(unittest.TestCase):
    def testThreeSumClosest(self):
        s = Solution()
        self.assertEqual(s.threeSumClosest(nums = [4,0,5,-5,3,3,0,-4,-5], target = -2), -2)
        self.assertEqual(s.threeSumClosest(nums = [-1,2,1,-4], target = 1), 2)
        self.assertEqual(s.threeSumClosest(nums = [0,0,0], target = 1), 0)


if __name__ == '__main__':
    unittest.main()