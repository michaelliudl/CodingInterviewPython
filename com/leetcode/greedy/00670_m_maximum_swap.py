from typing import List
import heapq

class Solution:
    # Greedy
    def maximumSwap(self, num: int) -> int:
        if num < 10: return num
        digits = []
        temp = num
        while temp > 0:
            last = temp % 10
            digits.append(last)
            temp //= 10
        digits.reverse()
        n = len(digits)
        for i in range(n-1):
            if digits[i] == 9:
                continue
            larger,lastLargerIndex = digits[i],-1
            for j in range(n-1, i, -1):
                if digits[j] > larger:
                    larger = digits[j]
                    lastLargerIndex = j
            if lastLargerIndex > i:
                digits[i],digits[lastLargerIndex] = digits[lastLargerIndex],digits[i]
                break
        ans = 0
        for i in range(len(digits)):
            ans = ans * 10 + digits[i]
        return ans
            


import unittest

class TestSolution(unittest.TestCase):
    def testMaximumSwap(self):
        s = Solution()
        self.assertEqual(s.maximumSwap(num = 98368), 98863)
        self.assertEqual(s.maximumSwap(num = 1993), 9913)
        self.assertEqual(s.maximumSwap(num = 2736), 7236)
        self.assertEqual(s.maximumSwap(num = 9973), 9973)


if __name__ == '__main__':
    unittest.main()