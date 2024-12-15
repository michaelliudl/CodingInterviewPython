from typing import List
import heapq

class Solution:

    # Heap for smallest and set for marking
    def findScore(self, nums: List[int]) -> int:
        heap = [(num, index) for index, num in enumerate(nums)]
        heapq.heapify(heap)
        marked = set()
        score = 0
        while heap:
            num, index = heapq.heappop(heap)
            if index not in marked:
                score += num
                marked.add(index)
                if index - 1 >= 0:
                    marked.add(index - 1)
                if index + 1 < len(nums):
                    marked.add(index + 1)
        return score


import unittest

class TestSolution(unittest.TestCase):
    def testMaxScore(self):
        s = Solution()
        self.assertEqual(s.maxScore(nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3), 12)
        self.assertEqual(s.maxScore(nums1 = [4,2,3,1,1], nums2 = [7,5,10,9,6], k = 1), 30)
        


if __name__ == '__main__':
    unittest.main()