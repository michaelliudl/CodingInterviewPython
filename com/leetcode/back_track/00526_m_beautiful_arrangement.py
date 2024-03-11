from typing import List

class Solution:
    def countArrangement(self, n: int) -> int:

        def recur(index, perm):
            nonlocal ans
            if len(perm) == n:
                ans += 1
                return
            for candidate in range(1, n + 1):
                if (candidate % index == 0 or index % candidate == 0) and candidate not in perm:
                    perm.add(candidate)
                    recur(index + 1, perm)
                    perm.remove(candidate)

        if n <= 1:
            return n
        ans = 0
        recur(index = 1, perm = set())
        return ans

import unittest

class TestSolution(unittest.TestCase):
    def testCountArrangement(self):
        s = Solution()
        self.assertEqual(s.countArrangement(n = 2), 2)
        self.assertEqual(s.countArrangement(n = 1), 1)
        


if __name__ == '__main__':
    unittest.main()