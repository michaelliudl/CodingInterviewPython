from typing import List
import heapq

class Solution:

    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        if not heights: return 0
        if len(heights) == 1: return 0
        heap = []
        for i in range(1, len(heights)):
            if heights[i] > heights[i-1]:
                # Use heap to track diffs. Greedily use bricks on small diffs.
                heapq.heappush(heap, (heights[i] - heights[i-1]))
                while len(heap) > ladders:
                    minDiff = heapq.heappop(heap)
                    bricks -= minDiff
                if bricks < 0:
                    return i-1
        return len(heights) - 1


import unittest

class TestSolution(unittest.TestCase):
    def testSuggestedProducts(self):
        s = Solution()
        self.assertEqual(s.suggestedProducts(products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"), 
                         [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]])
        self.assertEqual(s.suggestedProducts(products = ["havana"], searchWord = "havana"), 
                         [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]])


if __name__ == '__main__':
    unittest.main()