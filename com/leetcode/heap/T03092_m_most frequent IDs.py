from typing import List
import heapq
from sortedcontainers import SortedSet

class Solution:

    # def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
    #     result = []
    #     sortedSet = SortedSet()
    #     numToElem = {}
    #     for i in range(len(nums)):
    #         num = nums[i]
    #         if num in numToElem:
    #             numToElem[num][0] += freq[i]
    #         else:
    #             elem = [freq[i], num]
    #             numToElem[num] = elem
    #             sortedSet.add(elem)
    #         result.append(sortedSet[-1][0])
    #     return result
        

    # Heap time out
    def mostFrequentIDsHeap(self, nums: List[int], freq: List[int]) -> List[int]:
        heap = []
        numMap = {}
        n = len(nums)
        result = [0] * n
        for i in range(n):
            num = nums[i]
            if num not in numMap:
                elem = [-freq[i], num]
                numMap[num] = elem
                heapq.heappush(heap, elem)
            else:
                numMap[num][0] += -freq[i]
                heapq.heapify(heap)
            if heap:
                result[i] = -heap[0][0]
        return result


import unittest

class TestSolution(unittest.TestCase):
    def testMostFrequentIDs(self):
        s = Solution()
        self.assertEqual(s.mostFrequentIDs(nums = [2,3,2,1], freq = [3,2,-3,1]), [3,3,2,2])
        self.assertEqual(s.mostFrequentIDs(nums = [5,5,3], freq = [2,-2,1]), [2,0,1])
        


if __name__ == '__main__':
    unittest.main()