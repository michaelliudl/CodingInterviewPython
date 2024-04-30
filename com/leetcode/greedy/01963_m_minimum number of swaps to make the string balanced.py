from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def minSwaps(self, s: str) -> int:
        # Count number of [ that doesn't have a matching ]
        noMatchLeft = 0
        for char in s:
            if char == '[':
                noMatchLeft += 1
            elif noMatchLeft > 0:
                noMatchLeft -= 1
        # Get result based on no-matching left [ number is odd or even
        return (noMatchLeft // 2 + 1) if noMatchLeft & 1 else noMatchLeft // 2


import unittest

class TestSolution(unittest.TestCase):
    def testBagOfTokensScore(self):
        s = Solution()
        self.assertEqual(s.bagOfTokensScore(tokens = [33,4,28,24,96], power = 35), 3)
        self.assertEqual(s.bagOfTokensScore(tokens = [100], power = 50), 0)
        self.assertEqual(s.bagOfTokensScore(tokens = [200,100], power = 150), 1)
        self.assertEqual(s.bagOfTokensScore(tokens = [100,200,300,400], power = 200), 2)


if __name__ == '__main__':
    unittest.main()