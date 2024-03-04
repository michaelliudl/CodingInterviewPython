from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers or len(numbers) < 2:
            return []
        left, right = 0, len(numbers) - 1
        while left < right:
            curSum = numbers[left] + numbers[right]
            if curSum == target:
                return [left + 1, right + 1]
            elif curSum < target:
                left += 1
            else:
                right -= 1
        return []

import unittest

class TestSolution(unittest.TestCase):
    def testTwoSum(self):
        s = Solution()
        self.assertEqual(s.twoSum(numbers = [2,7,11,15], target = 9), [1,2])
        self.assertEqual(s.twoSum(numbers = [2,3,4], target = 6), [1,3])
        self.assertEqual(s.twoSum(numbers = [-1,0], target = -1), [1,2])


if __name__ == '__main__':
    unittest.main()