from typing import List, DefaultDict, Counter
import heapq

class Solution:

    # Greedy, count frequency and sort descending, assign first most frequent with 1 push
    def minimumPushes(self, word: str) -> int:
        counter = Counter(word)
        counts = [0] * 26
        for char in counter:
            counts[ord(char) - ord('a')] = counter[char]
        counts = [count for count in counts if count > 0]
        counts.sort(reverse=True)
        res = 0
        for i in range(len(counts) // 8 + 1):
            res += ((i + 1) * sum(counts[(i * 8):min(len(counts), ((i + 1) * 8))]))
        return res

import unittest

class TestSolution(unittest.TestCase):
    def testMinOperations(self):
        s = Solution()
        self.assertEqual(s.minOperations(k = 11), 5)
        self.assertEqual(s.minOperations(k = 1), 0)


if __name__ == '__main__':
    unittest.main()