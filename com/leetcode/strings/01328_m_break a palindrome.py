from typing import List

class Solution:

    # Replace first non 'a' character with 'a', if not palindrome, it's answer
    # If it's palindrome after replacing, it mean now it's all 'a'. Use original string and replace last character with 'b'
    # If no replacement happened, it means orignal string is all 'a'. Replace last with 'b'
    def breakPalindrome(self, palindrome: str) -> str:

        def isPalin(p):
            low, high = 0, len(p) - 1
            while low < high:
                if p[low] != p[high]:
                    return False
                low += 1
                high -= 1
            return True

        if not palindrome or len(palindrome) == 1:
            return ''
        palin = list(palindrome)
        isPalindrome = True
        replaced = False
        for i in range(len(palin)):
            if palin[i] != 'a':
                palin[i] = 'a'
                replaced = True
            if not isPalin(palin):
                isPalindrome = False
            if replaced:
                break
        if isPalindrome:
            if replaced:
                palin = list(palindrome)
            palin[-1] = 'b'
        return ''.join(palin)


import unittest

class TestSolution(unittest.TestCase):
    def testReorderLogFiles(self):
        s = Solution()
        self.assertEqual(s.reorderLogFiles(logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]), 
                         ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"])
        self.assertEqual(s.reorderLogFiles(logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]), 
                         ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"])

if __name__ == '__main__':
    unittest.main()