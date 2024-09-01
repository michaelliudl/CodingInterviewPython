from typing import List

class Solution:

    def nearestPalindromic(self, n: str) -> str:

        def findPalins(string):
            num = int(string)
            size = len(string)
            palins = []
            half = string[:(size + 1) // 2]
            reversedHalf = half[:(size // 2)][::-1]
            candidate = int(half + reversedHalf)

            if candidate < num:
                palins.append(candidate)
            else:
                prevHalf = str(int(half) - 1)
                reversedPrevHalf = prevHalf[:(size // 2)][::-1]
                if size % 2 == 0 and int(prevHalf) == 0:
                    palins.append(9)
                elif size % 2 == 0 and prevHalf == '9':
                    palins.append(int(prevHalf + '9' + reversedPrevHalf))
                else:
                    palins.append(int(prevHalf + reversedPrevHalf))
            
            if candidate > num:
                palins.append(candidate)
            else:
                nextHalf = str(int(half) + 1)
                reversedNextHalf = nextHalf[:(size // 2)][::-1]
                palins.append(int(nextHalf + reversedNextHalf))
            
            return palins

        prevPalin, nextPalin = findPalins(n)
        num = int(n)
        return str(prevPalin) if abs(prevPalin - num) <= abs(nextPalin - num) else str(nextPalin)


import unittest

class TestSolution(unittest.TestCase):
    def testNearestPalindromic(self):
        s = Solution()
        self.assertEqual(s.nearestPalindromic(n = "123"), "121")
        self.assertEqual(s.nearestPalindromic(n = "1"), "0")


if __name__ == '__main__':
    unittest.main()