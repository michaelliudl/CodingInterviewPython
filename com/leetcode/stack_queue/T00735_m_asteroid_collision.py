from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        pass

import unittest

class TestSolution(unittest.TestCase):
    def testSimplifyPath(self):
        s = Solution()
        self.assertEqual(s.simplifyPath("/home/"), "/home")
        self.assertEqual(s.simplifyPath("/../"), "/")
        self.assertEqual(s.simplifyPath("/home//foo/"), "/home/foo")



if __name__ == '__main__':
    unittest.main()