from typing import List
import heapq

class Solution:

    # Order by height then move elements to index of k
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        if not people: return None
        n=len(people)
        r=[]
        ppl=[[-h,k] for [h,k] in people]
        heapq.heapify(ppl)
        while ppl:
            [h,k]=heapq.heappop(ppl)
            r.insert(k, [-h,k])
        return r



import unittest

class TestSolution(unittest.TestCase):
    def testReconstructQueue(self):
        s = Solution()
        self.assertEqual(s.reconstructQueue(people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]), [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]])
        self.assertEqual(s.reconstructQueue(people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]), [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]])
        


if __name__ == '__main__':
    unittest.main()