from typing import List

class Solution:

    def sortSentence(self, s: str) -> str:
        if not s:
            return s
        sArr = s.split(' ')
        result = [''] * len(sArr)
        for string in sArr:
            index = -1
            elem = ''
            for i in range(len(string) - 1, -1, -1):
                if string[i] < '0' or string[i] > '9':
                    index = int(string[i + 1:]) - 1
                    elem = string[:i + 1]
                    break
            result[index] = elem
        return ' '.join(result)


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