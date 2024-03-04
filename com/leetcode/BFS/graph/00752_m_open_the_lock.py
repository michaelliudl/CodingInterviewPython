from typing import List,Deque

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadEndSet = set(deadends)
        if target in deadEndSet or '0000' in deadEndSet:
            return -1
        if target == '0000':
            return 0
        queue = Deque()
        visited = set()
        start = [0,0,0,0]
        queue.append((start, 0))        # Enqueue combinations and steps
        visited.add(tuple(start))
        while queue:
            combination, steps = queue.popleft()
            if ''.join([str(i) for i in combination]) == target:      # BFS, first time reaching target is shortest path
                return steps
            for i in range(4):
                for turn in (-1, 1):
                    nextComb = combination[:]
                    nextComb[i] = (10 + nextComb[i] + turn) % 10
                    if tuple(nextComb) not in visited and ''.join([str(i) for i in nextComb]) not in deadEndSet:
                        visited.add(tuple(nextComb))
                        queue.append((nextComb, steps + 1))
        return -1
        

import unittest

class TestSolution(unittest.TestCase):
    def testOpenLock(self):
        s = Solution()
        self.assertEqual(s.openLock(deadends = ["0000"], target = "8888"), -1)
        self.assertEqual(s.openLock(deadends = ["8888"], target = "0009"), 1)
        self.assertEqual(s.openLock(deadends = ["0201","0101","0102","1212","2002"], target = "0202"), 6)
        self.assertEqual(s.openLock(deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"), -1)
        


if __name__ == '__main__':
    unittest.main()