from typing import List
import heapq, math

class Solution:
    
    # Use max heap to maximize score
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = [-num for num in nums]
        heapq.heapify(heap)
        res = 0
        for _ in range(k):
            score = -heapq.heappop(heap)
            res += score
            heapq.heappush(heap, -math.ceil(score / 3))
        return res



import unittest

class TestSolution(unittest.TestCase):
    def testTopKFrequent(self):
        s = Solution()
        self.assertEqual(s.topKFrequent(words = ["i","love","leetcode","i","love","coding"], k = 2), ["i","love"])
        self.assertEqual(s.topKFrequent(words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4), ["the","is","sunny","day"])



if __name__ == '__main__':
    unittest.main()