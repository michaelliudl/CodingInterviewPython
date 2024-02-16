from typing import List

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if not word1 or not word2: return False
        if len(word1) != len(word2): return False
        chars1,chars2=[False]*26,[False]*26
        freq1,freq2=[0]*26,[0]*26
        for i in range(len(word1)):
            index1 = ord(word1[i]) - ord('a')
            chars1[index1] = True
            freq1[index1] += 1
            index2 = ord(word2[i]) - ord('a')
            chars2[index2] = True
            freq2[index2] += 1
        freq1.sort()
        freq2.sort()
        return chars1 == chars2 and freq1 == freq2

import unittest

class TestSolution(unittest.TestCase):
    def testCloseStrings(self):
        s = Solution()
        self.assertEqual(s.closeStrings(word1 = "uau", word2 = "ssx"), False)
        self.assertEqual(s.closeStrings(word1 = "abc", word2 = "bca"), True)
        self.assertEqual(s.closeStrings(word1 = "cabbba", word2 = "abbccc"), True)
        self.assertEqual(s.closeStrings(word1 = "a", word2 = "aa"), False)

if __name__ == '__main__':
    unittest.main()