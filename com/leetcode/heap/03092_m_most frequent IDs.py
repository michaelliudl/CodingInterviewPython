from typing import List, DefaultDict
import heapq
from sortedcontainers import SortedList

class Solution:

    # Max Heap to track most frequency
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        heap = []
        numFreq = DefaultDict(int)
        n = len(nums)
        result = [0] * n
        for i in range(n):
            num = nums[i]
            numFreq[num] += freq[i]
            heapq.heappush(heap, (-numFreq[num], num))  # Push num's latest frequency to max heap
            while numFreq[heap[0][1]] < -heap[0][0]:    # Pop from max heap if heap top number's frequency in map is actually less than frequency of same element at heap top
                                                        # Otherwise need to maintain whole heap and TLE
                heapq.heappop(heap)
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