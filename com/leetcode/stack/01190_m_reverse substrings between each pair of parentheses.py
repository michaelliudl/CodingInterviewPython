from typing import List

class Solution:

    # O(n**2)
    def reverseParentheses(self, s: str) -> str:

        def rev(start):
            low, high = start, len(chars) - 1
            while low < high:
                chars[low], chars[high] = chars[high], chars[low]
                low += 1
                high -= 1

        revStarts = []
        chars = []
        for i, char in enumerate(s):
            if char not in '()':
                chars.append(char)
            elif char == '(':
                revStarts.append(len(chars))    # Length of existing chars is starting index for next reverse
            else:
                rev(revStarts.pop())
        return ''.join(chars)


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