from typing import List, Deque

class Solution:

    # Josephus iterative, O(n) time, O(1) space
    def findTheWinner(self, n: int, k: int) -> int:
        res = 0
        for remPeople in range(1, n + 1):
            res = (res + k) % remPeople
        return res + 1

    # Josephus recursive, O(n) time/space
    def findTheWinnerRecur(self, n: int, k: int) -> int:

        def josephus(n, k):
            if n == 1:
                return 0
            return (josephus(n - 1, k) + k) % n
        
        return josephus(n, k) + 1

    # Simulate with queue, O(nk)
    def findTheWinnerSim(self, n: int, k: int) -> int:
        queue = Deque()
        for i in range(n):
            queue.append(i + 1)
        while len(queue) > 1:
            for _ in range(k - 1):
                queue.append(queue.popleft())
            queue.popleft()
        return queue[0]


import unittest

class TestSolution(unittest.TestCase):
    def testFindTheWinner(self):
        s = Solution()
        self.assertEqual(s.findTheWinner(n = 5, k = 2), 3)
        self.assertEqual(s.findTheWinner(n = 6, k = 5), 1)


if __name__ == '__main__':
    unittest.main()