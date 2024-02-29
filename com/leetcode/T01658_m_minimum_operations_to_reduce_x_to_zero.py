from typing import List,Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    # def __eq__(self, __value: object) -> bool:
    #     return isinstance(__value, ListNode) and self.val == __value.val and self.next == __value.next

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        ans = 1
        while left <= right:
            if x - nums[left] == 0 or x - nums[right] == 0:
                return ans
            if x - nums[left] < 0 and x - nums[right] < 0:
                return -1
            if x - nums[left] < 0:
                x -= nums[right]
                right -= 1
            elif x - nums[right] < 0:
                x -= nums[left]
                left += 1
            else:
                x -= max(nums[left], nums[right])
                if nums[left] >= nums[right]:
                    left += 1
                else:
                    right -= 1
            ans += 1
        return ans if x == 0 else -1

import unittest

class TestSolution(unittest.TestCase):
    def testMinOperations(self):
        s = Solution()
        self.assertEqual(s.minOperations(nums = [1,1], x = 3), -1)
        self.assertEqual(s.minOperations(nums = [1,1,4,2,3], x = 5), 2)
        self.assertEqual(s.minOperations(nums = [5,6,7,8,9], x = 4), -1)
        self.assertEqual(s.minOperations(nums = [3,2,20,1,1,3], x = 10), 5)


if __name__ == '__main__':
    unittest.main()