from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if not arr:
            return arr
        numAndIndex = [(num, index) for index, num in enumerate(arr)]
        numAndIndex.sort()
        result = [1] * len(arr)
        curNum = numAndIndex[0][0]
        rank = 1
        for i in range(1, len(arr)):
            num, index = numAndIndex[i]
            if num > curNum:
                curNum = num
                rank += 1
            result[index] = rank
        return result

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def testSortColors(self):
        input = [2,0,2,1,1,0]
        expected = [0,0,1,1,2,2]
        self.s.sortColors(input)
        self.assertEqual(input, expected)

if __name__ == '__main__':
    unittest.main()