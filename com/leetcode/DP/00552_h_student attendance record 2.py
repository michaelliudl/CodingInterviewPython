from typing import List, DefaultDict

class Solution:

    # Based on condition, there can be 0 or 1 'A' and 0 or 1 or 2 'L' (2 'L's are consecutive)
    # Use 2x3 matrix to save states of 2 'A' choices and 3 'L' choices (or a hashmap of 6 keys tuples from combination of above 'A' and 'L' choices)
    def checkRecord(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        # Base case n == 1
        states = {
            # 'P'       'L'
            (0, 0): 1, (0, 1): 1, (0, 2): 0,    # 0 'A'
            # 'A'
            (1, 0): 1, (1, 1): 0, (1, 2): 0     # 1 'A'
        }
        for _ in range(n - 1):
            temp = DefaultDict(int)

            # Choose 'P'
            temp[(0, 0)] = (states[(0, 0)] + states[(0, 1)] + states[(0, 2)]) % MOD
            temp[(1, 0)] = (states[(1, 0)] + states[(1, 1)] + states[(1, 2)]) % MOD

            # Choose 'L'
            temp[(0, 1)] = states[(0, 0)]
            temp[(1, 1)] = states[(1, 0)]
            temp[(0, 2)] = states[(0, 1)]
            temp[(1, 2)] = states[(1, 1)]

            # Choose 'A'
            temp[(1, 0)] += (states[(0, 0)] + states[(0, 1)] + states[(0, 2)]) % MOD

            states = temp
        return sum(states.values()) % MOD

import unittest

class TestSolution(unittest.TestCase):
    def testFindItinerary(self):
        s = Solution()
        self.assertEqual(s.canCross(stones = [0,1,3,5,6,8,12,17]), True)
        self.assertEqual(s.canCross(stones = [0,1,2,3,4,8,9,11]), False)

if __name__ == '__main__':
    unittest.main()