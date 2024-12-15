from typing import List, Deque

class Solution:

    # Convert array to string, use queue to try swapping '0' with another number, use set to track tried results
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        m, n = 2, 3
        goal = '123450'
        start = []
        for i in range(m):
            for j in range(n):
                start.append(str(board[i][j]))
        startStr = ''.join(start)
        if startStr == goal:
            return 0
        
        queue = Deque()
        queue.append(startStr)
        visited = set()
        visited.add(startStr)
        
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        step = 1
        while queue:
            curLen = len(queue)
            for size in range(curLen, 0, -1):
                curStr = queue.popleft()
                zeroIndex = curStr.index('0')
                i = zeroIndex // n
                j = zeroIndex % n
                for dx, dy in dirs:
                    x, y = i + dx, j + dy
                    if 0 <= x < m and 0 <= y < n:
                        swappedIndex = x * n + y
                        strList = list(curStr)
                        strList[zeroIndex] = curStr[swappedIndex]
                        strList[swappedIndex] = curStr[zeroIndex]
                        newStr = ''.join(strList)
                        if newStr == goal:
                            return step
                        if newStr not in visited:
                            queue.append(newStr)
                            visited.add(newStr)
            step += 1
        return -1

import unittest

class TestSolution(unittest.TestCase):
    def testSlidingPuzzle(self):
        s = Solution()
        self.assertEqual(s.slidingPuzzle(board = [[1,2,3],[4,0,5]]), 1)
        self.assertEqual(s.slidingPuzzle(board = [[1,2,3],[5,4,0]]), -1)
        self.assertEqual(s.slidingPuzzle(board = [[4,1,2],[5,0,3]]), 5)

if __name__ == '__main__':
    unittest.main()