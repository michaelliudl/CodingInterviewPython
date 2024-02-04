from typing import List
import heapq

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        if not costs or k<=0 or candidates<=0: return 0
        n=len(costs)
        if n<=k: return sum(costs)
        heap = []
        usedLeft, usedRight = 0, n-1
        for i in range(candidates):
            if i < usedRight:
                heapq.heappush(heap, (costs[i], i))
                usedLeft = i
            if n-1-i > usedLeft:
                heapq.heappush(heap, (costs[n-1-i], n-1-i))
                usedRight = n-1-i
        ans = 0
        for _ in range(k):
            cost, index = heapq.heappop(heap)
            ans += cost
            if index <= usedLeft and usedLeft < usedRight - 1:
                usedLeft += 1
                heapq.heappush(heap, (costs[usedLeft], (usedLeft)))
            if index >= usedRight and usedRight > usedLeft + 1:
                usedRight -= 1
                heapq.heappush(heap, (costs[usedRight], (usedRight)))
        return ans
        




import unittest

class TestSolution(unittest.TestCase):
    def testTotalCost(self):
        s = Solution()
        self.assertEqual(s.totalCost(costs = [28,35,21,13,21,72,35,52,74,92,25,65,77,1,73,32,43,68,8,100,84,80,14,88,42,53,98,69,64,40,60,23,99,83,5,21,76,34], k = 32, candidates = 12), 
                         1407)
        self.assertEqual(s.totalCost(costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4), 11)
        self.assertEqual(s.totalCost(costs = [1,2,4,1], k = 3, candidates = 3), 4)



if __name__ == '__main__':
    unittest.main()