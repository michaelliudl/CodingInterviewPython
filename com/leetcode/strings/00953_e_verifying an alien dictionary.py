from typing import List

class Solution:

    def isAlienSorted(self, words: List[str], order: str) -> bool:

        def outOfOrder(first, second):
            return order.index(first) < order.index(second)

        def isAlien(start, end, level):
            if start >= end:
                return True
            minLen = min(len(words[i]) for i in range(start, end + 1))
            maxLen = max(len(words[i]) for i in range(start, end + 1))
            if level == minLen:         # Reach the end of shortest string prefix
                if minLen == maxLen:    # Same strings
                    return True
                i = start + 1
                while i <= end:
                    if len(words[i]) < len(words[i - 1]):   # Prefix should be before prefix + more
                        return False
                    elif len(words[i]) > len(words[i - 1]): # Same prefix, still more characters
                        return isAlien(i, end, level)
                    i += 1
            left = start
            i = start + 1
            while i <= end:
                if words[i][level] != words[i - 1][level]:
                    if outOfOrder(words[i][level], words[i - 1][level]):    # Check if first character difference is out of order
                        return False
                    if not isAlien(left, i - 1, level + 1):                 # Check if strings with same prefix are out of order in deeper levels
                        return False
                    left = i
                i += 1
            return isAlien(left, end, level + 1)        # Last few strings with same prefix

        if not words or not order:
            return False
        result = isAlien(start = 0, end = len(words) - 1, level = 0)
        return result


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