from typing import List
from typing import Deque


class Solution:

    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        left, right = 0, n - 1
        while left < n - 1 and arr[left + 1] >= arr[left]:  # Move left until decreasing, potentially to remove subarray to the right
            left += 1
        while right > 0 and arr[right - 1] <= arr[right]:   # Move right until increasing, potentially to remove subarray to the left
            right -= 1
        # Case 1: remove subarray after left
        # Case 2: remove subarray before right
        res = min(n - (left + 1), right)
        # Case 3: remove subarray between left and right.
        i, j = left, n - 1
        while i >= 0 and j >= right and i < j:
            if arr[i] <= arr[j]:
                j -= 1
            else:
                i -= 1
            res = min(res, j - i)
        return res


import unittest

class TestSolution(unittest.TestCase):
    def testFindLengthOfShortestSubarray(self):
        s = Solution()
        self.assertEqual(s.findLengthOfShortestSubarray(arr = [1,2,3,10,4,2,3,5]), 3)
        self.assertEqual(s.findLengthOfShortestSubarray(arr = [5,4,3,2,1]), 4)
        self.assertEqual(s.findLengthOfShortestSubarray(arr = [1,2,3]), 0)
        self.assertEqual(s.findLengthOfShortestSubarray(arr = [1,2,3,10,0,7,8,9]), 2)



if __name__ == '__main__':
    unittest.main()