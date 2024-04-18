from typing import List

class Solution:

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if not flowerbed:
            return False
        for i in range(len(flowerbed)):
            if n == 0:
                break
            if flowerbed[i] == 1:
                continue
            if i == 0:
                if len(flowerbed) == 1 or (len(flowerbed) > 1 and flowerbed[i + 1] == 0):
                    flowerbed[i] = 1
                    n -= 1
            elif i == len(flowerbed) - 1:
                if i - 1 >= 0 and flowerbed[i - 1] == 0:
                    flowerbed[i] = 1
                    n -= 1
            else:
                if flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    n -= 1
        return n == 0

        

import unittest

class TestSolution(unittest.TestCase):

    def testCanPlaceFlowers(self):
        s=Solution()
        self.assertEqual(s.canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 1), True)
        self.assertEqual(s.canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 2), False)
        self.assertEqual(s.canPlaceFlowers(flowerbed = [0], n = 1), True)

if __name__ == '__main__':
    unittest.main()