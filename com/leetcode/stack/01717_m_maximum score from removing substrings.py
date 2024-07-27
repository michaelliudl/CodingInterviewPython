from typing import List

class Solution:

    # Use stack to handle removal, greedily remove higher score substring first
    def maximumGain(self, s: str, x: int, y: int) -> int:
        remove1, remove2 = 'ab', 'ba'
        high, low = x, y
        if x < y:
            remove1, remove2 = 'ba', 'ab'
            high, low = y, x
        res = 0
        stack1 = []
        for char in s:
            if stack1 and stack1[-1] == remove1[0] and char == remove1[-1]:
                res += high
                stack1.pop()
            else:
                stack1.append(char)
        stack2 = []
        for char in stack1:
            if stack2 and stack2[-1] == remove2[0] and char == remove2[-1]:
                res += low
                stack2.pop()
            else:
                stack2.append(char)
        return res

import unittest

class TestSolution(unittest.TestCase):
    def testReverseParentheses(self):
        s = Solution()
        self.assertEqual(s.reverseParentheses(s = "(abcd)"), "dcba")
        self.assertEqual(s.reverseParentheses(s = "(u(love)i)"), "iloveu")
        self.assertEqual(s.reverseParentheses(s = "(ed(et(oc))el)"), "leetcode")
        self.assertEqual(s.reverseParentheses(s = "f(ul)ao(t(y)qbn)()sj"), "fluaonbqytsj")



if __name__ == '__main__':
    unittest.main()