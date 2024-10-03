from typing import List

class Solution:

    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        cur = 1
        while len(result) < n:
            result.append(cur)
            if cur * 10 <= n:
                cur *= 10
            else:
                while cur % 10 == 9 or cur == n:
                    cur //= 10
                cur += 1
        return result

    def lexicalOrderBrute(self, n: int) -> List[int]:
        return [int(s) for s in (list(sorted([str(num) for num in range(1, n + 1)])))]

        

import unittest

class TestSolution(unittest.TestCase):

    def testLexicalOrder(self):
        s = Solution()
        self.assertEqual(s.lexicalOrder(n = 13), [1,10,11,12,13,2,3,4,5,6,7,8,9])
        self.assertEqual(s.lexicalOrder(n = 2), [1,2])
        self.assertEqual(s.lexicalOrder(n = 10), [1,10,2,3,4,5,6,7,8,9])

if __name__ == '__main__':
    unittest.main()