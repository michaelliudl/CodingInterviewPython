from typing import List

class Solution:

    def canArrange(self, arr: List[int], k: int) -> bool:
        count = [0] * k
        for num in arr:
            num %= k
            if num >= 0:
                count[num] += 1
            else:
                count[num + k] += 1
        res = count[0] % 2 == 0
        if res:
            for i in range(1, k // 2 + 1):
                if count[i] != count[k - i]:
                    return False
            return True
        return False


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