from typing import List
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        d={}
        for n in nums:
            d[n]=d[n]+1 if n in d else 1
        h=[]
        for e,c in d.items():
            if len(h)<k:
                heapq.heappush(h,[c,e])
            elif c>h[0][0]:
                heapq.heappop(h)
                heapq.heappush(h,[c,e])
        return [e[1] for e in h]



import unittest

class TestSolution(unittest.TestCase):
    def testTopKFrequent(self):
        s = Solution()
        self.assertEqual(set(s.topKFrequent([1,1,1,2,2,3],k=2)), set([1,2]))
        self.assertEqual(s.topKFrequent([1],k=1), [1])



if __name__ == '__main__':
    unittest.main()