from typing import List

class Solution:

    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        totalCount = len(rolls) + n
        totalSum = mean * totalCount
        missingSum = totalSum - sum(rolls)
        if missingSum < n or missingSum > n * 6:    # Outside range of n 1s or 6s
            return []
        res = [missingSum // n] * n         # Start with mean value
        for i in range(missingSum % n):     # Distribute remainder evenly, can also distribute in other ways
            res[i] += 1
        return res


import unittest

class TestSolution(unittest.TestCase):
    def testRotate(self):
        s = Solution()
        matrix = [[1,2,3],[4,5,6],[7,8,9]]
        s.rotate(matrix)
        self.assertEqual(matrix, [[7,4,1],[8,5,2],[9,6,3]])
        matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
        s.rotate(matrix)
        self.assertEqual(matrix, [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]])

if __name__ == '__main__':
    unittest.main()