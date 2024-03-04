from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    # Sort then greedily use power on small tokens for more score, then use score on large tokens for more power
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        if not tokens:
            return 0
        maxScore, score = 0, 0
        tokens.sort()
        left, right = 0, len(tokens) - 1
        while left <= right and (power >= tokens[left] or score):
            while left <= right and power >= tokens[left]:
                power -= tokens[left]
                left += 1
                score += 1
                maxScore = max(maxScore, score)
            if left <= right and score > 0:
                power += tokens[right]
                right -= 1
                score -= 1
        return maxScore


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