from typing import List

class Solution:

    def buddyStrings(self, s: str, goal: str) -> bool:
        if not s or not goal or len(s) != len(goal):
            return False
        # Must swap, if equal, then must have duplicate characters
        if s == goal and len(set(s)) < len(s):
            return True
        diffIndex = -1
        swapped = False
        for i in range(len(s)):
            if s[i] != goal[i]:
                if swapped:
                    return False
                if diffIndex < 0:
                    diffIndex = i
                elif s[diffIndex] != goal[i] or s[i] != goal[diffIndex]:
                    return False
                else:
                    swapped = True
        return swapped


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