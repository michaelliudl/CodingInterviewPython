from typing import List

class Solution:

    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in (s + s)


import unittest

class TestSolution(unittest.TestCase):
    def testIsAlienSorted(self):
        s = Solution()
        self.assertEqual(s.isAlienSorted(words = ["hello","hello"], order = "abcdefghijklmnopqrstuvwxyz"), True)
        self.assertEqual(s.isAlienSorted(words = ["hello","hellob","helloa"], order = "hlabcdefgijkmnopqrstuvwxyz"), False)
        self.assertEqual(s.isAlienSorted(words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"), True)
        self.assertEqual(s.isAlienSorted(words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"), False)
        self.assertEqual(s.isAlienSorted(words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"), False)
        

if __name__ == '__main__':
    unittest.main()