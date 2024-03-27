from typing import List

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        if not time:
            return 0
        result = 0
        remMap = {}
        for i in range(len(time)):
            rem = time[i] % 60
            remDiff = 60 - rem if rem > 0 else 0
            if remDiff in remMap:
                result += len(remMap[remDiff])
            if rem not in remMap:
                remMap[rem] = set()
            remMap[rem].add(i)
        return result

import unittest

class TestSolution(unittest.TestCase):
    def testNumPairsDivisibleBy60(self):
        s = Solution()
        self.assertEqual(s.numPairsDivisibleBy60(time = [30,20,150,100,40]), 3)
        self.assertEqual(s.numPairsDivisibleBy60(time = [60,60,60]), 3)



if __name__ == '__main__':
    unittest.main()