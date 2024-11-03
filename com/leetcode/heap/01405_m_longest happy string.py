from typing import List
import heapq

class Solution:

    # User max heap to track count of each char added to result
    def longestDiverseStringHeap(self, a: int, b: int, c: int) -> str:
        heap = []
        if a > 0:
            heapq.heappush(heap, (-a, 'a'))
        if b > 0:
            heapq.heappush(heap, (-b, 'b'))
        if c > 0:
            heapq.heappush(heap, (-c, 'c'))
        res = ''
        while heap:
            count, char = heapq.heappop(heap)
            if len(res) > 1 and res[-1] == res[-2] == char:
                if not heap:
                    break
                count2, char2 = heapq.heappop(heap)
                res += char2
                count2 += 1
                if count2 != 0:
                    heapq.heappush(heap, (count2, char2))
            else:
                res += char
                count += 1
            if count != 0:
                heapq.heappush(heap, (count, char))
        return res

    # Greedily choose largest number of characters
    def longestDiverseString(self, a: int, b: int, c: int) -> str:

        # Use pair of (num, char) to keep correct order when swapping parameters
        def helper(paramA, paramB, paramC):
            if paramA[0] < paramB[0]:
                return helper(paramB, paramA, paramC)
            if paramB[0] < paramC[0]:
                return helper(paramA, paramC, paramB)
            if paramB[0] == 0:
                return (paramA[1] * min(paramA[0], 2))
            useA = min(paramA[0], 2)
            useB = 1 if (paramA[0] - useA) >= paramB[0] else 0
            return (paramA[1] * useA) + (paramB[1] * useB) + helper((paramA[0] - useA, paramA[1]), (paramB[0] - useB, paramB[1]), paramC)
        
        return helper((a, 'a'), (b, 'b'), (c, 'c'))



import unittest

class TestSolution(unittest.TestCase):
    def testLongestDiverseString(self):
        s = Solution()
        self.assertIn(s.longestDiverseString(a = 1, b = 1, c = 7), 
                      ['ccaccbcc', 'ccbccacc'])
        self.assertIn(s.longestDiverseString(a = 7, b = 1, c = 0), 
                      ['aabaa'])
        


if __name__ == '__main__':
    unittest.main()