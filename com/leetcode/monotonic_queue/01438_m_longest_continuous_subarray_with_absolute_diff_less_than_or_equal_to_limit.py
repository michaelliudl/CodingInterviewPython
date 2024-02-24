from typing import List,Deque
import heapq

class Solution:

    # Use two queues to track min / max value index in a sliding window
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if not nums: return 0
        minQueue,maxQueue = Deque(),Deque()
        left,ans = 0,0
        for i in range(len(nums)):
            rightIndex,rightValue = i, nums[i]
            while minQueue and rightValue < nums[minQueue[-1]]:
                minQueue.pop()
            while maxQueue and rightValue > nums[maxQueue[-1]]:
                maxQueue.pop()
            minQueue.append(rightIndex)
            maxQueue.append(rightIndex)
            while nums[maxQueue[0]] - nums[minQueue[0]] > limit:
                if left == maxQueue[0]:
                    maxQueue.popleft()
                if left == minQueue[0]:
                    minQueue.popleft()
                left += 1
            ans = max(ans, rightIndex - left + 1)
        return ans

import unittest

class TestSolution(unittest.TestCase):
    def testKClosest(self):
        s = Solution()
        self.assertEqual(sorted(s.kClosest(points = [[1,3],[-2,2]], k = 1)), sorted([[-2,2]]))
        self.assertEqual(sorted(s.kClosest(points = [[3,3],[5,-1],[-2,4]], k = 2)), sorted([[3,3],[-2,4]]))



if __name__ == '__main__':
    unittest.main()