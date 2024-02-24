from typing import List

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        if not secret or not guess or not len(secret)==len(guess): return ''
        n=len(secret)
        bulls = 0
        secretCount, guessCount = [0]*10, [0]*10
        for i in range(n):
            if secret[i]==guess[i]:
                bulls += 1
            else:
                secretCount[int(secret[i])] += 1
                guessCount[int(guess[i])] += 1
        cows = 0
        for i in range(10):
            cows += min(secretCount[i], guessCount[i])
        return str(bulls)+'A'+str(cows)+'B'

import unittest

class TestSolution(unittest.TestCase):
    def testTwoSum(self):
        s = Solution()
        self.assertEqual(s.twoSum([2,7,11,15],9), [0,1])
        self.assertEqual(s.twoSum([3,2,4],6), [1,2])
        self.assertEqual(s.twoSum([3,3],6), [0,1])


if __name__ == '__main__':
    unittest.main()