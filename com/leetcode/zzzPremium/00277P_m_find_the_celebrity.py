from typing import List

# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:

    def findCelebrity(self, n: int) -> int:
        candidate = 0
        for i in range(1, n):           # Find candidate that doesn't know any others
            if knows(candidate, i):
                candidate = i
        # Everyone else should know candidate
        for i in range(n):
            # Candidate found after `i`, need to check if candiate knows `i`
            if i < candidate and knows(candidate, i):
                return -1
            if i != candidate and (not knows(i, candidate)):
                return -1
        return candidate

    # Use graph, time out O(n**2)
    def findCelebrityGraph(self, n: int) -> int:
        def fill(i, j):
            if knows(i, j):
                if i not in graphKnow:
                    graphKnow[i] = set()
                graphKnow[i].add(j)
                if j not in graphKnown:
                    graphKnown[j] = set()
                graphKnown[j].add(i)

        if n <= 1:
            return -1
        graphKnow = {}
        graphKnown = {}
        for i in range(n):
            for j in range(i + 1, n):
                fill(i, j)
                fill(j, i)
        for i in range(n):
            if (i not in graphKnow or not graphKnow[i]) and (i in graphKnown and len(graphKnown[i]) == n - 1):
                return i
        return -1



import unittest

class TestSolution(unittest.TestCase):
    def testMinAddToMakeValid(self):
        s = Solution()
        self.assertEqual(s.minAddToMakeValid("())"), 1)
        self.assertEqual(s.minAddToMakeValid("((("), 3)


if __name__ == '__main__':
    unittest.main()