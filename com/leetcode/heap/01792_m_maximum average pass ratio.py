from typing import List
import heapq

class Solution:

    # Use max heap to keep adding extra student to classes that can get maximum extra pass ratio
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        
        def extraRatio(passNum, total):
            return ((passNum + 1) / (total + 1)) - (passNum / total)
        
        heap = [(-extraRatio(passNum, total), passNum, total) for passNum, total in classes]
        heapq.heapify(heap)

        for _ in range(extraStudents):
            _, passNum, total = heapq.heappop(heap)
            heapq.heappush(heap, (-extraRatio(passNum + 1, total + 1), (passNum + 1), (total + 1)))
        
        return sum((passNum / total) for _, passNum, total in heap) / len(heap)




import unittest

class TestSolution(unittest.TestCase):
    def testMaxScore(self):
        s = Solution()
        self.assertEqual(s.maxScore(nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3), 12)
        self.assertEqual(s.maxScore(nums1 = [4,2,3,1,1], nums2 = [7,5,10,9,6], k = 1), 30)
        


if __name__ == '__main__':
    unittest.main()