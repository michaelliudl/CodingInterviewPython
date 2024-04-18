from typing import List

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        n, winLen = len(nums), 2 * k + 1
        ans = [-1] * n
        if n < winLen:
            return ans
        curSum = sum(nums[:winLen])
        for i in range(k, n - k):
            ans[i] = curSum // winLen
            if i < n - k - 1:
                curSum -= nums[i - k]
                curSum += nums[i + k + 1]
        return ans


import unittest

class TestSolution(unittest.TestCase):
    def testGetAverages(self):
        s = Solution()
        self.assertEqual(s.getAverages(nums = [7,4,3,9,1,8,5,2,6], k = 3), 
                         [-1,-1,-1,5,4,4,-1,-1,-1])
        self.assertEqual(s.getAverages(nums = [100000], k = 0), [100000])
        self.assertEqual(s.getAverages(nums = [8], k = 100000), [-1])


if __name__ == '__main__':
    unittest.main()