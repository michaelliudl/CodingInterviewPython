from typing import List
import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        if not words or k <= 0: return []
        cache={}
        for word in words:
            if word in cache:
                cache[word] -= 1
            else:
                cache[word] = -1
        heap = []
        for word in cache:
            heapq.heappush(heap, (cache[word], word))
        ans=[]
        for _ in range(k):
            _, word = heapq.heappop(heap)
            ans.append(word)
        return ans
        



import unittest

class TestSolution(unittest.TestCase):
    def testTopKFrequent(self):
        s = Solution()
        self.assertEqual(s.topKFrequent(words = ["i","love","leetcode","i","love","coding"], k = 2), ["i","love"])
        self.assertEqual(s.topKFrequent(words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4), ["the","is","sunny","day"])



if __name__ == '__main__':
    unittest.main()