from typing import List
class Solution:

    # For loop outside, two pointer inside
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return [[]]
        nums.sort()
        n = len(nums)
        result = []
        for i in range(n - 3):
            # Skip duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                # Skip duplicates
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                low, high = j + 1, n - 1
                while low < high:
                    curSum = nums[i] + nums[j] + nums[low] + nums[high]
                    if curSum == target:
                        result.append([nums[i], nums[j], nums[low], nums[high]])
                        low += 1
                        high -= 1
                        # Skip duplicates
                        while low < high and nums[low] == nums[low - 1]:
                            low += 1
                        while low < high and nums[high] == nums[high + 1]:
                            high -= 1
                    elif curSum < target:
                        low += 1
                    else:
                        high -= 1
        return result



import unittest

class TestSolution(unittest.TestCase):
    def testFourSum(self):
        s = Solution()
        self.assertEqual(s.fourSum(nums = [-3,-1,0,2,4,5], target = 2), [[-3,-1,2,4]])
        self.assertEqual(s.fourSum(nums = [-3,-1,0,2,4,5], target = 1), [[-3,-1,0,5]])
        self.assertEqual(s.fourSum(nums = [-2,-1,-1,1,1,2,2], target = 0), [[-2,-1,1,2],[-1,-1,1,1]])
        self.assertEqual(s.fourSum(nums = [1,0,-1,0,-2,2], target = 0), [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]])
        self.assertEqual(s.fourSum(nums = [2,2,2,2,2], target = 8), [[2,2,2,2]])


if __name__ == '__main__':
    unittest.main()