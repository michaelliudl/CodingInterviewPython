from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return ['']
        if n == 1:
            return ['()']
        result = set()
        subGens = self.generateParenthesis(n - 1)
        for sub in subGens:
            result.add('()' + sub)
            result.add(sub + '()')
            for i, ch in enumerate(sub):
                if ch == '(':
                    result.add(sub[:i+1] + '()' + sub[i+1:])
        return list(result)

        

import unittest

class TestSolution(unittest.TestCase):
    def testGenerateParenthesis(self):
        s = Solution()
        self.assertEqual(s.generateParenthesis(n = 1), ['()'])
        self.assertEqual(s.generateParenthesis(n = 3), ["((()))","(()())","(())()","()(())","()()()"])
        


if __name__ == '__main__':
    unittest.main()