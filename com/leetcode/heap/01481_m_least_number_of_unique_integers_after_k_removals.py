from typing import List
import heapq

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        if not arr or len(arr)<=k: return 0
        count = {}
        for elem in arr:
            count[elem] = count.get(elem, 0) + 1
        heap = []
        for elem,c in count.items():
            heapq.heappush(heap, (c,elem))
        i = 0
        while i < k:
            c, _ = heap[0]
            if k - i >= c:
                heapq.heappop(heap)
                i += c
            else:
                i = k
        return len(heap)



import unittest

class TestSolution(unittest.TestCase):
    def testFindLeastNumOfUniqueInts(self):
        s = Solution()
        self.assertEqual(s.findLeastNumOfUniqueInts(arr = [1,1,2,2,3,3], k = 3), 2)
        self.assertEqual(s.findLeastNumOfUniqueInts(arr = [5,5,4], k = 1), 1)
        self.assertEqual(s.findLeastNumOfUniqueInts(arr = [4,3,1,1,3,3,2], k = 3), 2)



if __name__ == '__main__':
    unittest.main()