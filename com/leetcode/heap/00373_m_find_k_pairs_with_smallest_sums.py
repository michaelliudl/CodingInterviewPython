from typing import List
import heapq

class Solution:

    # Push size k min heap with sum of digits from array A plus first digit from array B.
    # Then pop and keep pushing sum of later digits from array B with popped digit from array A.
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2 or k<=0: return []
        h=[]
        for i in range(min(k, len(nums1))):
            curSum = nums1[i] + nums2[0]
            heapq.heappush(h, (curSum, i, 0))
        ans=[]
        while h and len(ans) < k:
            _, index1, index2 = heapq.heappop(h)
            ans.append([nums1[index1], nums2[index2]])
            if index2 + 1 < len(nums2):
                nextSum = nums1[index1] + nums2[index2 + 1]
                heapq.heappush(h, (nextSum, index1, index2 + 1))
        return ans

import unittest

class TestSolution(unittest.TestCase):

    def testKSmallestPairs(self):
        s=Solution()
        self.assertEqual(s.kSmallestPairs(nums1 = [1,7,11], nums2 = [2,9,10], k = 3), [[1,2],[7,2],[1,9]])
        self.assertEqual(s.kSmallestPairs(nums1 = [1,2], nums2 = [3], k = 3), [[1,3],[2,3]])
        self.assertEqual(s.kSmallestPairs(nums1 = [1,7,11], nums2 = [2,4,6], k = 3), [[1,2],[1,4],[1,6]])
        self.assertEqual(s.kSmallestPairs(nums1 = [1,1,2], nums2 = [1,2,3], k = 2), [[1,1],[1,1]])

if __name__ == '__main__':
    unittest.main()