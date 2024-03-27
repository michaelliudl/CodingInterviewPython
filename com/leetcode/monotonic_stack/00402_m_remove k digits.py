from typing import List
from typing import Deque


class Solution:

    def removeKdigits(self, num: str, k: int) -> str:
        if not num:
            return ''
        if k >= len(num):
            return '0'
        stack = []
        for char in num:
            while k > 0 and stack and stack[-1] > char:
                stack.pop()
                k -= 1
            stack.append(char)
        for _ in range(k):
            stack.pop()
        result = []
        for char in stack:
            if char != '0' or result:
                result.append(char)
        return ''.join(result) if result else '0'



import unittest

class TestSolution(unittest.TestCase):
    def testRemoveKdigits(self):
        s = Solution()
        self.assertEqual(s.removeKdigits(num = "10001", k = 1), '0')
        self.assertEqual(s.removeKdigits(num = "1432219", k = 3), '1219')
        self.assertEqual(s.removeKdigits(num = "10200", k = 1), '200')
        self.assertEqual(s.removeKdigits(num = "10", k = 2), '0')
        self.assertEqual(s.removeKdigits(num = "112", k = 1), '11')



if __name__ == '__main__':
    unittest.main()