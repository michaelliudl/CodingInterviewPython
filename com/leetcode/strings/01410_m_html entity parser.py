from typing import List

class Solution:

    def entityParser(self, text: str) -> str:
        if not text:
            return text
        result = []
        i, n = 0, len(text)
        while i < n:
            html = False
            if text[i] == '&':
                if i + 6 < n and text[i: i + 7] == '&frasl;':
                    result.append('/')
                    i += 7
                    html = True
                if not html and i + 5 < n:
                    sub = text[i: i + 6]
                    if sub == '&quot;':
                        result.append('"')
                        i += 6
                        html = True
                    elif sub == '&apos;':
                        result.append('\'')
                        i += 6
                        html = True
                if not html and i + 4 < n and text[i: i + 5] == '&amp;':
                    result.append('&')
                    i += 5
                    html = True
                if not html and i + 3 < n:
                    sub = text[i : i + 4]
                    if sub == '&gt;':
                        result.append('>')
                        i += 4
                        html = True
                    elif sub == '&lt;':
                        result.append('<')
                        i += 4
                        html = True
            if not html:
                result.append(text[i])
                i += 1
        return ''.join(result)

    
                       


import unittest

class TestSolution(unittest.TestCase):
    def testMyAtoi(self):
        s = Solution()
        self.assertEqual(s.myAtoi(s = "   +0 123"), 0)
        self.assertEqual(s.myAtoi(s = "00000-42a1234"), 0)
        self.assertEqual(s.myAtoi(s = "   -42"), -42)
        self.assertEqual(s.myAtoi(s = "42"), 42)
        self.assertEqual(s.myAtoi(s = "+-12"), 0)
        self.assertEqual(s.myAtoi(s = "words and 987"), 0)
        self.assertEqual(s.myAtoi(s = "4193 with words"), 4193)
        

if __name__ == '__main__':
    unittest.main()