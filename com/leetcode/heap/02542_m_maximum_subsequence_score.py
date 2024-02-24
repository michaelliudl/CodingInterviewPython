from typing import List
import heapq

class Solution:

    # Similar to 1383
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if len(nums1) != len(nums2): return 0
        n = len(nums1)
        combinations = []
        for i in range(n):
            combinations.append((nums2[i], nums1[i]))
        combinations.sort(reverse=True)     # Sort reversely for picking small to multiply
        ans,curSum = 0,0
        heap = []
        for toMulti,toSum in combinations:
            heapq.heappush(heap, toSum)     # Heap to maintain largest possible sums
            curSum += toSum
            if len(heap) == k:              # Difference, choose exactly k, while 1383 choose at most k
                ans = max(ans, (curSum * toMulti))
                smallest = heapq.heappop(heap)
                curSum -= smallest
        return ans




import unittest

class TestSolution(unittest.TestCase):
    def testMaxScore(self):
        s = Solution()
        self.assertEqual(s.maxScore(nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3), 12)
        self.assertEqual(s.maxScore(nums1 = [4,2,3,1,1], nums2 = [7,5,10,9,6], k = 1), 30)
        


if __name__ == '__main__':
    unittest.main()