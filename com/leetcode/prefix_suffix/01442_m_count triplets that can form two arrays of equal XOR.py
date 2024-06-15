from typing import List, DefaultDict

class Solution:

    # Prefix XOR array, O(n**2)
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        xorPrefix = [0] * (n + 1)
        xorCur = 0
        for i in range(n):
            xorCur ^= arr[i]
            xorPrefix[i + 1] = xorCur
        res = 0
        for j in range(1, n):
            for i in range(0, j):
                a = xorPrefix[j] ^ xorPrefix[i]
                for k in range(j, n):
                    b = xorPrefix[k + 1] ^ xorPrefix[j]
                    if a == b:
                        res += 1
        return res

        

        

import unittest

class TestSolution(unittest.TestCase):

    def testCountTriplets(self):
        s=Solution()
        self.assertEqual(s.countTriplets(arr = [2,3,1,6,7]), 4)
        self.assertEqual(s.countTriplets(arr = [1,1,1,1,1]), 10)

if __name__ == '__main__':
    unittest.main()