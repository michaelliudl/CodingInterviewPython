from typing import List,Deque

class Solution:

    # Prefix sum and monotonic queue
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefixSum = [0] * (n + 1)
        for i, num in enumerate(nums):
            prefixSum[i + 1] = prefixSum[i] + num
        queue = Deque()

        res = n + 1
        for i in range(n + 1):
            while queue and (prefixSum[i] - prefixSum[queue[0]]) >= k:
                res = min(res, (i - queue[0]))
                queue.popleft()
            while queue and prefixSum[i] <= prefixSum[queue[-1]]:
                queue.pop()
            queue.append(i)
        return res if res <= n else -1


import unittest

class TestSolution(unittest.TestCase):
    def testShortestSubarray(self):
        s = Solution()
        self.assertEqual(s.shortestSubarray(nums = [1], k = 1), 1)
        self.assertEqual(s.shortestSubarray(nums = [1,2], k = 4), -1)
        self.assertEqual(s.shortestSubarray(nums = [2,-1,2], k = 3), 3)
        self.assertEqual(s.shortestSubarray(nums = [17,85,93,-45,-21], k = 150), 2)

if __name__ == '__main__':
    unittest.main()