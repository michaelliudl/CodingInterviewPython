from typing import List

class Solution:

    def countMaxOrSubsets(self, nums: List[int]) -> int:

        def dfs(index, path):
            nonlocal res
            if index == len(nums):
                if path == maxOr:
                    res += 1
                return
            dfs(index + 1, path)
            dfs(index + 1, path | nums[index])

        maxOr = 0
        for num in nums:
            maxOr |= num
        res = 0
        dfs(index=0, path=0)
        return res

        

import unittest

class TestSolution(unittest.TestCase):

    def testSequentialDigits(self):
        s = Solution()
        self.assertEqual(s.sequentialDigits(low = 100, high = 300), [123,234])
        self.assertEqual(s.sequentialDigits(low = 1000, high = 13000), [1234,2345,3456,4567,5678,6789,12345])

if __name__ == '__main__':
    unittest.main()