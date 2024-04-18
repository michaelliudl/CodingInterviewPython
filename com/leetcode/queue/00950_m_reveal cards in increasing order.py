from typing import List,Deque

class Solution:

    # Simulate process with queue of index of sorted array
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        if not deck:
            return deck
        deck.sort()
        queue = Deque()
        for i in range(len(deck)):
            queue.append(i)
        result = [0] * len(deck)
        for i in range(len(deck)):
            result[queue.popleft()] = deck[i]
            if queue:
                queue.append(queue.popleft())
        return result

import unittest

class TestSolution(unittest.TestCase):
    def testDeckRevealedIncreasing(self):
        s = Solution()
        self.assertEqual(s.deckRevealedIncreasing(deck = [17,13,11,2,3,5,7]), [2,13,3,11,5,17,7])
        self.assertEqual(s.deckRevealedIncreasing(deck = [1,1000]), [1,1000])


if __name__ == '__main__':
    unittest.main()