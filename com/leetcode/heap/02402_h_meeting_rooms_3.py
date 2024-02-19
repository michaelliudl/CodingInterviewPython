from typing import List
import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        if n<=0 or not meetings: return 0
        endingSoon = []
        count = [0]*n
        occupied = [False]*n
        heapq.heapify(meetings)
        # meetings.sort()
        while meetings:
        # for start, end in meetings:
            start, end = heapq.heappop(meetings)
            while endingSoon and start >= endingSoon[0][0]:
                _, lastIndex = heapq.heappop(endingSoon)
                occupied[lastIndex] = False
            firstAvail = n
            for i in range(n):          # Use heap to speed up finding first available meeting room
                if not occupied[i]:
                    firstAvail = i
                    break
            firstAvailEnd = end
            if firstAvail == n and endingSoon:
                nextEnd, nextIndex = heapq.heappop(endingSoon)
                firstAvailEnd = (nextEnd + (end - start))
                firstAvail = nextIndex
            count[firstAvail] += 1
            occupied[firstAvail] = True
            heapq.heappush(endingSoon, (firstAvailEnd, firstAvail))
        maxCount, maxIndex = 0,0
        for i in range(n):
            if count[i] > maxCount:
                maxCount = count[i]
                maxIndex = i
        return maxIndex



import unittest

class TestSolution(unittest.TestCase):
    def testMostBooked(self):
        s = Solution()
        self.assertEqual(s.mostBooked(n = 4, meetings = [[12,44],[27,37],[48,49],[46,49],[24,44],[32,38],[21,49],[13,30]]), 1)
        self.assertEqual(s.mostBooked(n = 2, meetings = [[0,10],[1,5],[2,7],[3,4]]), 0)
        self.assertEqual(s.mostBooked(n = 3, meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]), 1)
        self.assertEqual(s.mostBooked(n = 2, meetings = [[0,10],[1,5],[2,7],[3,4]]), 0)
        self.assertEqual(s.mostBooked(n = 100, meetings = [[0,1]]), 0)



if __name__ == '__main__':
    unittest.main()