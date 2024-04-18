from typing import List

class Solution:

    # Binary search to find the smallest index that has at least `k` missing positive integers before it
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if not arr:
            return k
        low, high = 0, len(arr)
        while low < high:
            mid = low + (high - low) // 2
            if arr[mid] - mid - 1 >= k:
                high = mid
            else:
                low = mid + 1
        return low + k

    # O(n)
    def findKthPositive1(self, arr: List[int], k: int) -> int:
        if not arr:
            return k
        missing = 1
        for num in arr:
            diff = num - missing
            if diff < k:
                k -= diff
                missing = num + 1
            else:
                return missing + k - 1
        return arr[-1] + k


import unittest

class TestSolution(unittest.TestCase):
    def testRotate(self):
        s = Solution()
        matrix = [[1,2,3],[4,5,6],[7,8,9]]
        s.rotate(matrix)
        self.assertEqual(matrix, [[7,4,1],[8,5,2],[9,6,3]])
        matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
        s.rotate(matrix)
        self.assertEqual(matrix, [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]])

if __name__ == '__main__':
    unittest.main()